from inventory.models import Videogame, Genre, Platform
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from cart.models import ShoppingCartHistory


# Create your views here.
def store(request):
    main_videogames = Videogame.get_random_videogames(6)
    best_videogames = Videogame.get_random_videogames(10)
    featured_videogames = Videogame.get_random_videogames(4)
    popular_videogames = Videogame.get_random_videogames(6)

    context = {
        "main_videogames": main_videogames,
        "best_videogames": best_videogames,
        "featured_videogames": featured_videogames,
        "popular_videogames": popular_videogames,
    }

    return render(request, "store/store.html", context)


def watch_videogame(request, id):
    videogame = Videogame.get(id=id)
    best_selling_videogames = Videogame.get_random_videogames(6)

    context = {
        "videogame": videogame,
        "best_selling_videogames": best_selling_videogames,
    }

    return render(request, "store/store_videogame.html", context)


def purchase_history(request):
    purchase_history = ShoppingCartHistory.get_history_cart_user(request)

    context = {"purchase_history": purchase_history}

    return render(request, "store/purchase_history.html", context)


def try_luck(request):
    return redirect("ver_videojuego", Videogame.get_random_videogames().id)


def watch_genre_videogames(request, genre=None):
    genre = Genre.get(genre)
    videogames = Videogame.get_videogames_by_genre(genre, 16)

    context = {"genre": genre, "videogames": videogames}

    return render(request, "store/genre_videogames.html", context)


def watch_platform_videogames(request, platform=None):
    platform = Platform.get(platform)
    all_platforms = Platform.get_all_platforms()
    videogames = Videogame.get_videogames_by_platform(platform, 16)
    popular_videogames = Videogame.get_videogames_by_platform(platform, 6)

    context = {
        "platform": platform,
        "all_platforms": all_platforms,
        "videogames": videogames,
        "popular_videogames": popular_videogames,
    }

    return render(request, "store/platform_videogames.html", context)


@require_POST
def search(request):
    search = request.POST.get("search")
    videogames = Videogame.search(search)
    all_platforms = Platform.get_all_platforms()

    context = {
        "search": search,
        "videogames": videogames,
        "all_platforms": all_platforms,
    }

    return render(request, "store/search.html", context)


@require_POST
def search_by_price(request):
    search = request.POST.get("search")
    videogames = Videogame.search_by_price(search)
    all_platforms = Platform.get_all_platforms()

    context = {
        "search": search,
        "videogames": videogames,
        "all_platforms": all_platforms,
    }

    return render(request, "store/search_by_price.html", context)
