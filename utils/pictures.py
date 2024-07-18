from inventory.models import Videogame
from blog.models import Post


def get_latest_pictures(limit=0):
    posts = Post.get_latest_pictures()
    videogames = Videogame.get_latest_pictures()

    pictures = posts.union(videogames).order_by("-created")

    if limit > 0:
        return pictures[:limit]

    return pictures[:6]


