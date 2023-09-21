from dotenv import load_dotenv
import os
import base64
from requests import post, get
import urllib
import pandas as pd



def get_token(client_id_spotify, client_secret_spotify):
    auth_string = client_id_spotify + ":" + client_secret_spotify
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
    }

    data = {
            "grant_type": "client_credentials"
            }

    result = post(url, headers=headers, data=data)

    return result.json()["access_token"]


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_anything(token, artist_name, type):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist_name}&type={type}&limit=1"

    query_url = url + "?" + query 
    
    result = get(query_url, headers=headers)
    
    return result.json()


def list_playlist(token, playlist_id, limit=100, offset=0):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    
    filter = "items(added_at,track(id, name, artists(name), popularity, duration_ms))"
    filter = urllib.parse.quote_plus(filter)
    filter = "fields="+filter
    filter = filter + f"&limit={limit}&offset={offset}"

    url = url + '?' + filter
    headers = get_auth_header(token)
    
    result = get(url, headers=headers)

    return result.json()

def insert_musics_in_df(df, songs):
    for song in songs['items']:
        new_row = { 
                    "id_track":     song['track']['id'], 
                    "name":         song['track']['name'],
                    "added_at":     song['added_at'],
                    "artists":      ' - '.join([thing['name'] for thing in song['track']['artists']]),
                    "duration_ms":  song['track']['duration_ms'],
                    "popularity":   song['track']['popularity'],
                }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    return df

def get_total_music_playlist(token, id_playlist):
    url = f'https://api.spotify.com/v1/playlists/{id_playlist}?fields=tracks.total'
    headers = get_auth_header(token)
    result = get(url,headers=headers)

    return int(result.json()['tracks']['total'])


def get_musics_playlist(client_id_spotify, client_secret_spotify, playlist_name):

    token = get_token(client_id_spotify, client_secret_spotify)
    playlist = search_for_anything(token, playlist_name, type="playlist")
    id_playlist = playlist['playlists']['items'][0]['id']
    total_musica_playlist = get_total_music_playlist(token, id_playlist)

    df = pd.DataFrame(columns=["id_track", "name", "added_at", "artists", "duration_ms", "popularity" ])

    offset = 0
    while offset < total_musica_playlist:

        songs = list_playlist(token, id_playlist, limit=50, offset=offset)
        df = insert_musics_in_df(df, songs)

        offset+=50

    df['added_at'] =  pd.to_datetime(df['added_at'])

    df = df.sort_values(by=["added_at", "popularity"],ascending=False).reset_index(drop=True)

    return df
    

def teste():
    return "teste"