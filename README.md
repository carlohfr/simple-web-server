# Simple Web Server

This is a simple web server build in python and socket library


## How to install

- Clone this repository

```
git clone https://github.com/carlohfr/simple-web-server.git
```

- Go to the project directory

```
cd simple-web-server
```

- Run start command

```
python exemple.py
```

- Then go to localhost:8000 


## How to use 

- Import the library.

```
from simplewebserver import SimpleWebServer
```

- Create server object

```
server = SimpleWebServer()
```

- Set a route

```
server.get("/", <your-handler-function>)
```

**Important:** your handler functions need to have 2 arguments. The first is the request string, and the second is response object. For exemple:


```
def index(req, res):
    res.send_file("index.html")
```

- Pass server options

```
server.start(port=8000, public_files_directory="public")
```


## Project structure

- ```public``` directory: All your static files goes here.

- ```simplewebserver``` directory: All server scripts goes here.
