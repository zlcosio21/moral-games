from youtubesearchpython import VideosSearch

def video(videojuego):
    search = VideosSearch(videojuego, limit=1)
    results = search.result()

    if results["result"]:
        full_link = results["result"][0]["link"]
        video_id = full_link.split("v=")[1]

    return video_id