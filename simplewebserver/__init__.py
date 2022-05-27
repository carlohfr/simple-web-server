# Project: Simple Web Server
# Created: 01/10/2018
# Revised: 27/05/2022
# Version: 1.1
# License: MIT


from .socket_server import SocketServer
from .response import Response


class SimpleWebServer:

    def __init__(self):
        self.__RECV_BUFFER = 1024
        self.__get_callbacks = {}


    def __get_request_info(self, req):
        request = req.decode("utf-8").split("\r\n", 1)
        request = request[0].split(" ")
        return {"request-type": request[0], "request-url": request[1]}


    def __handler(self, conn, addr):
        req = conn.recv(self.__RECV_BUFFER)
        res = Response(conn)
        req_info = self.__get_request_info(req)
        
        if req_info["request-type"] == "GET":            
            self.__get_callbacks[req_info["request-url"]](req, res)


    def get(self, url, function):
        self.__get_callbacks[url] = function


    def start(self, port=8080):
        self.__server = SocketServer()
        self.__server.start(port, self.__handler)
