from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
ACCESS_KEY= os.environ["ACCESS_KEY"]
SECRET_KEY= os.environ["SECRET_KEY"]
ENDPOINT_SERVER= os.environ["ENDPOINT_SERVER"]

def main():
    
    bucket_name = datetime.today().strftime("%d-%m-%Y")
    
    current_dir = os.getcwd()
    current_dir = os.path.join(current_dir, "data")
    file_name = "file_test.txt"

    # Create a cliente and access the server running in docker.
    client = Minio(
        ENDPOINT_SERVER,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=False  #if true we need config SSL.
    )
    
    
    # verifica se o bucket existe, se não existe cria
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
    else:
        print(f"Bucket '{bucket_name}' already exists")

    # Upload 'current_dir+file_name' as object name
    # 'file_name' to bucket 'bucket_name'.
    client.fput_object( bucket_name, file_name, os.path.join(current_dir, file_name))
    print(
        f"'{os.path.join(current_dir, file_name)}' is successfully uploaded as "
        f"object '{file_name}' to bucket '{bucket_name}'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)