import socket

IP = '127.0.0.1'
PORTA = 8000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Define o tipo do servido neste caso TCP/IP.
servidor.bind((IP, PORTA))                                    # Informa o IP e a PORTA do servidor.
servidor.listen(5)                                            # Numero maximo de maquinas que podem conectar.


# Informações para o console
print("Servidor iniciado...")
print("Servidor na porta:",PORTA)
print("Servidor no endreço:",IP)


while True:
    conexao, endereco = servidor.accept()                  # Aceita a conexão.
    requisicao = conexao.recv(1024).decode('utf-8')        # Converte e armazena a requisição(Não usado no codigo).

    try:                                                   # Tratamento de erros.
        file = open("index.html", 'rb')                    # Abre o arquivo(APENAS HTML), r => read , b => byte format.
        resposta = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'
        tipoarquivo = 'text/html'

        header += 'Content-Type: ' + str(tipoarquivo) + '\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        resposta = '<html><meta charset= "utf-8"><body><center><h3>Erro 404: Arquivo não encontrado</h3>' \
                   '<p>Servidor Python</p></center></body></html>'.encode('utf-8')


    respostafinal = header.encode('utf-8')       # Converte o header pra bytes.
    respostafinal += resposta                    # Concatena a resposta com header.
    conexao.send(respostafinal)                  # Envia a resposta final para o cliente.
    conexao.close()
