[![author](https://img.shields.io/badge/author-guilhermemaioli-red.svg)](https://www.linkedin.com/in/guilherme-maioli/) [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-365/) 


# Working with MinIO
Minio is an object storage server that implements the same public API as Amazon S3. This means that applications that can be configured to talk to Amazon S3 can also be configured to talk to Minio.


## Putting server online 
We uploaded the server in a Docker container. Acessing the cmd in the folder project e running:
```sh
docker compose up
```

## Using Python

### Install dependencies Python
After we are going to install dependencies from Python.
```sh
pip install -r requeriments.txt
```

### Set .env with your informations
ACCESS_KEY, SECRET_KEY and ENDPOINT_SERVER are informations for MinIO. CLIENT_ID_SPOTIFY and CLIENT_SECRET_SPOTIFY are informations for Spotify.
```sh

ACCESS_KEY="access-key-minio"

SECRET_KEY="secret-key-minio"

ENDPOINT_SERVER="endpoint-runserver-minio"

CLIENT_ID_SPOTIFY="your-client-id-spotify"

CLIENT_SECRET_SPOTIFY="your-client-secret-spotify"

```

### Running Python
Next step is to run the Python Script. Type the following command into CMD. In *playlistname* enter the name of the playlist name you want. 
```sh
python main.py --playlist "Choose a playlist name"
```
 After that, the file with the playlist will be in the bucket named <current_date>.

## Using AWS CLI
Let's do everything manually using AWS CLI

### Configuring AWS CLI credentials
```sh
> aws configure
AWS Access Key ID [None]: your_key_access
AWS Secret Access Key [None]: your_secret_key
Default region name [None]: us-east-1
Default output format [None]: ENTER
```

### To make a bucket
```sh
> aws --endpoint-url https://your_url:9000 s3 mb s3://bucket_name
## mesage return
make_bucket: s3://bucket_name/
```

### To add an object to a bucket
```sh
## file_send must have complete path
> aws --endpoint-url https://your_url:9000 s3 cp file_send s3://bucket_name
## mesage return
upload: ./file_send to s3://mybucket/simplejson-3.3.0.tar.gz
```

