# Project: Simple Web Server
# Created: 01/10/2018
# Revised: 27/05/2022
# Version: 1.1
# License: MIT


import os

from .socket_server import SocketServer
from .response import Response


class SimpleWebServer:

    def __init__(self):
        self.__RECV_BUFFER = 1024
        self.__get_callbacks = {}
        self.__public_files = []


    def __save_public_files_names(self, public_files_directory):
        for root, directory_names, file_names in os.walk(public_files_directory):
            for file in file_names:
                self.__public_files.append("/" + os.path.join(root, file))


    def __get_request_info(self, req):
        request = req.decode("utf-8").split("\r\n", 1)
        request = request[0].split(" ")
        return {"request-type": request[0], "request-url": request[1]}


    def __handler(self, conn, addr):
        req = conn.recv(self.__RECV_BUFFER)
        res = Response(conn)
        req_info = self.__get_request_info(req)
        
        if req_info["request-type"] == "GET":
            if req_info["request-url"] in self.__get_callbacks:
                self.__get_callbacks[req_info["request-url"]](req, res)
            elif req_info["request-url"] in self.__public_files:
                res.send_file(req_info["request-url"])
            else:
                res.send_404_page()


    def get(self, url, function):
        self.__get_callbacks[url] = function


    def start(self, port=8080, public_files_directory="public"):
        self.__save_public_files_names(public_files_directory)
        self.__server = SocketServer()
        self.__server.start(port, self.__handler)
