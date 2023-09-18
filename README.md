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

## Set Access Key and Secret Key in .env
```sh
ACCESS_KEY="your_access_key"

SECRET_KEY="your_secret_key"
```