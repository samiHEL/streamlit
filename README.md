## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)


## General Info
***
The goal is to put our streamlit project in docker container
## Technologies
***
A list of technologies used within the project(first look requirements.txt):
* [Python](https://www.python.org/downloads/release/python-380/): Version 3.8
* [Streamlit](https://streamlit.io/)
* [seaborn,matplotlib,numpy,pandas]
* [Docker](https://www.docker.com/)
## Installation
***
Introduction to docker:

-> Docker makes it possible to set up an efficient application deployment system, in a way that is adaptable to any server.Prepare easy-to-deploy development environments using containers.

-> We orchestrate our containers (docker image) with docker compose and we create an image with the Dockerfile.

-> An executable image built from a text file (Dockerfile) that contains precise instructions (like a blueprint) for making containers in series.

-> docker-compose.yaml → operation of several containers together.

Advantage:

-> New lighter virtualization system → containers.
-> Shares resources with the host system.
-> Only works with Linux
-> Starts up quickly.

Basic docker command:

https://stockagesami.blob.core.windows.net/conteneur-1/dockercheatsheet8.png

docker run -d -p 80:80 docker/streamlit

-> -d- Run the container in detached mode (in the background). While continuing to use the terminal.

-> -p 80:80- Map the host port 80 to the container port 80. To access the tutorial, open a web browser and go to http://localhost:80. If you already have a service that listens on port 80 on your host machine, you can specify another port. For example, specify -p 3000:80 and then access the tutorial via a web browser at http://localhost:3000.

-> docker/streamlit:01 Specify the image to use with version.

Dockerfile example:

https://stockagesami.blob.core.windows.net/conteneur-1/Capture%20d%E2%80%99%C3%A9cran%20du%202022-10-30%2014-32-38.png


