from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
from datetime import datetime
import argparse

from spotify import get_musics_playlist

load_dotenv()

ACCESS_KEY= os.environ["ACCESS_KEY"]
SECRET_KEY= os.environ["SECRET_KEY"]
ENDPOINT_SERVER= os.environ["ENDPOINT_SERVER"]
CLIENT_ID_SPOTIFY= os.environ["CLIENT_ID_SPOTIFY"]
CLIENT_SECRET_SPOTIFY= os.environ["CLIENT_SECRET_SPOTIFY"]


def save_file_with_playlist(playlist_name):
    
    df = get_musics_playlist(CLIENT_ID_SPOTIFY, CLIENT_SECRET_SPOTIFY, playlist_name)
    filename = playlist_name.replace(" ", "_") + "_" + datetime.today().strftime("%d-%m-%Y") + ".json"
    df.to_json(f"./data/{filename}", orient="index")

    return filename

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--playlistname', dest="playlistname", type=str, help="Add playlistname")
    args = parser.parse_args()
    if args.playlistname is None:
        print("Inform a playlist name with '--playlistname <name>'.")
        return
    
    playlist_name = args.playlistname

    bucket_name = datetime.today().strftime("%d-%m-%Y")
    
    current_dir = os.getcwd()
    current_dir = os.path.join(current_dir, "data")
    
    file_name = save_file_with_playlist(playlist_name)

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