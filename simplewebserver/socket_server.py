# Project: Simple Web Server
# Created: 01/10/2018
# Revised: 27/05/2022
# Version: 1.1
# License: MIT


import socket


class SocketServer:

    def __init__(self):
        pass


    def start(self, port, callback):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port))                                    
        sock.listen(5)

        print(f"Server starts on port {port}")                                            

        while True:
            conn, addr = sock.accept()
            callback(conn, addr)
            conn.close()
