from inventory.models import Videogame, Genre
from utils.slider_images import random_slider


def slider(request):
    slider = random_slider()

    return {"slider": slider}


def sidebar(request):
    popular_videogames = Videogame.get_random_videogames(3)
    all_genres = Genre.get_all_genres()

    context = {
        "popular_videogames_sidebar": popular_videogames,
        "all_genres_sidebar": all_genres,
    }

    return context
