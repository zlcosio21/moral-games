import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
PASSWORD_API_KEY = os.getenv("PASSWORD_API_KEY")
api_key = PASSWORD_API_KEY
youtube = build('youtube', 'v3', developerKey=api_key)

def video(videojuego):
    search_response = youtube.search().list(
        q=videojuego,
        type="video",
        part="id",
        maxResults=1
    ).execute()

    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']

    return video_id
