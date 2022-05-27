# Project: Simple Web Server
# Created: 01/10/2018
# Revised: 27/05/2022
# Version: 1.1
# License: MIT


from simplewebserver import SimpleWebServer

server = SimpleWebServer()


def index(req, res):
    res.send_page("index.html")

server.get("/", index)

server.start(port=8000)
