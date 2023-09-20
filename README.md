[![author](https://img.shields.io/badge/author-guilhermemaioli-red.svg)](https://www.linkedin.com/in/guilherme-maioli/) [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-365/) 

# Technologies 
<p align="left">  
  <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
</p> 


# Working DataLake with MinIO
Minio is an object storage server that implements the same public API as Amazon S3. This means that applications that can be configured to talk to Amazon S3 can also be configured to talk to Minio.

## Putting server online 
We uploaded the server in a Docker container. Acessing the cmd in the folder project e running:
```sh
docker compose up
```

## Install dependencies Python
After we are going to install dependencies from Python.
```sh
pip install -r requeriments.txt
```

## Set .env with your informations
```sh
ACCESS_KEY="your_access_key"

SECRET_KEY="your_secret_key"

ENDPOINT_SERVER="your_url"
```