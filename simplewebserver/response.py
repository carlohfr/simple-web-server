# Project: Simple Web Server
# Created: 01/10/2018
# Revised: 27/05/2022
# Version: 1.1
# License: MIT


class Response:

    def __init__(self, conn):
        self.__conn = conn
        self.__file_types = {"html":"text/html", "css": "text/css", "js": "text/javascript", "jpg": "image/jpg", "png": "image/png", "jpeg": "image/jpeg", "gif": "image/gif", "webm": "video/webm", "mp4": "video/mp4", "ogg": "audio/ogg", "audio/wav": "audio/wav"}


    def send_file(self, filepath):
        try:
            filepath = filepath.replace("/", "", 1)                                                   
            file = open(filepath, 'rb')
            content = file.read()
            file.close()

            header = 'HTTP/1.1 200 OK\n'
            file_extension = filepath.rsplit('.', 1)[1]

            if file_extension in self.__file_types:
                filetype = self.__file_types[file_extension]

                header += 'Content-Type: ' + str(filetype) + '\n\n'

        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            content = '<html><meta charset= "utf-8"><body><center><h3>Error 404: Not Found</h3><p>Simple Web Server</p></center></body></html>'.encode('utf-8')

        header = header.encode('utf-8')
        content = header + content
        self.__conn.send(content)


    def send_404_page(self):
        header = 'HTTP/1.1 404 Not Found\n\n'
        content = '<html><meta charset= "utf-8"><body><center><h3>Error 404: Not Found</h3><p>Simple Web Server</p></center></body></html>'.encode('utf-8')

        header = header.encode('utf-8')
        content = header + content
        self.__conn.send(content)
