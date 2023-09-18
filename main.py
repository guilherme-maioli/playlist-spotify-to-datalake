from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

def main():
    ACCESS_KEY= os.environ["ACCESS_KEY"]
    SECRET_KEY= os.environ["SECRET_KEY"]

    current_dir = os.getcwd()
    bucket_name = "bucket2"
    file_name = "file_test.txt"

    # Cria um cliente e acessa o servidor rodando em docker.
    client = Minio(
        "127.0.0.1:9000",
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=False
    )

    
    
    # verifica se o bucket existe, se não existe cria
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
    else:
        print(f"Bucket '{bucket_name}' already exists")

    # Upload 'C:\\Users\\Guilherme\\Desktop\\portifolio\\remove_backgroung.png' as object name
    # 'remove_backgroung.png' to bucket 'bucket1'.
    client.fput_object(
        bucket_name, file_name, os.path.join(current_dir, file_name),
    )
    print(
        f"'{os.path.join(current_dir, file_name)}' is successfully uploaded as "
        f"object '{file_name}' to bucket '{bucket_name}'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)