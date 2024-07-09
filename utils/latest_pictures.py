from inventory.models import Videogame
from blog.models import Post


def get_latest_pictures():
    posts = Post.get_latest_pictures()
    videogames = Videogame.get_latest_pictures()

    pictures = posts.union(videogames).order_by("-created")

    return pictures[:6]