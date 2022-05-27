# Project: Simple Web Server
# Created: 01/10/2018
# Revised: 27/05/2022
# Version: 1.1
# License: MIT


class Response:

    def __init__(self, conn):
        self.__conn = conn


    def send_page(self, filepath):
        try:                                                   
            file = open(filepath, 'rb')
            content = file.read()
            file.close()

            header = 'HTTP/1.1 200 OK\n'
            filetype = 'text/html'

            header += 'Content-Type: ' + str(filetype) + '\n\n'

        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            content = '<html><meta charset= "utf-8"><body><center><h3>Error 404: File not found</h3><p>Simple Web Server</p></center></body></html>'.encode('utf-8')

        header = header.encode('utf-8')
        content = header + content
        self.__conn.send(content)
