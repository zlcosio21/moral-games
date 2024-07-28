from utils.pictures import get_latest_pictures
from inventory.models import Videogame, Genre
from django.shortcuts import render
from blog.models import Post


# Create your views here.
def gallery(request):
    latest_pictures = get_latest_pictures(12)
    all_genres = Genre.get_all_genres(4)

    context = {
        "latest_pictures": latest_pictures,
        "all_genres": all_genres,
    }

    return render(request, "gallery/gallery.html", context)


def watch_gallery_genre(request, id):
    genre = Genre.get_by_id(id)
    all_genres = Genre.get_all_genres(4)
    pictures_videogames = Videogame.get_pictures_by_genre(genre, all=True)
    pictures_posts = Post.get_pictures_by_genre(genre, all=True)
    all_pictures = Genre.get_all_pictures(pictures_videogames, pictures_posts)

    context = {"genre": genre, "all_genres": all_genres, "all_pictures": all_pictures}

    return render(request, "gallery/gallery_genre.html", context)
