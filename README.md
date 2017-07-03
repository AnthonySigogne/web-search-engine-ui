# web-search-engine-ui
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

UI of the simple web search engine https://github.com/AnthonySigogne/web-search-engine

## DEMO
A demo can be found here : http://searchengine.byprog.com/  

About 500 French URLs and 500 English URLs of the news network http://www.france24.com/ have been indexed.

## INSTALL AND RUN

### REQUIREMENTS
This tool requires *Python3+* and the web search engine API (see link above).

### WITH PIP
```
git clone https://github.com/AnthonySigogne/web-search-engine-ui.git
cd web-search-engine-ui
pip install -r requirements.txt
```

Then, run the tool :
```
FLASK_APP=index.py HOST=<ip> PORT=<port> flask run --port 80
```
Where :
* `ip` + `port` : route to web search engine API

To run in debug mode, prepend `FLASK_DEBUG=1` to the command :
```
FLASK_DEBUG=1 ... flask run --port 80
```

### WITH DOCKER
To run the tool with Docker, you can use my DockerHub image :
https://hub.docker.com/r/anthonysigogne/web-search-engine-ui/
```
docker run -p 80:5000 \
-e "HOST=<ip>" \
-e "PORT=<port>" \
anthonysigogne/web-search-engine-ui
```
Where :
* `ip` + `port` : route to web search engine API

Or, build yourself a Docker image :
```
git clone https://github.com/AnthonySigogne/web-search-engine-ui.git
cd web-search-engine-ui
docker build -t web-search-engine-ui .
```

## USAGE AND EXAMPLES
To use the search engine, just type this endpoint in your web browser : http://localhost/

![Web search engine](images/search-engine.png?raw=true "Search Engine" )

## LICENCE
MIT
