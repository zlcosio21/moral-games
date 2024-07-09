from django.views.decorators.http import require_POST
from utils.latest_pictures import get_latest_pictures
from django.shortcuts import render, redirect
from utils.emails import send_email_contact
from utils.messages import success_message
from inventory.models import Videogame
from blog.models import Post


# Create your views here.
def home(request):
    latest_news = Post.get_latest_posts(6)
    main_latest_news = Post.get_latest_posts(4)
    latest_posts = Post.get_latest_posts(2)
    tabbed_news = Post.get_tabbed_news()
    genres_with_posts = Post.get_all_genres_post()
    latest_pictures = get_latest_pictures()
    best_selling_videogames = Videogame.get_random_videogames(6)

    context = {
        "latest_news": latest_news,
        "main_latest_news": main_latest_news,
        "latest_posts": latest_posts,
        "tabbed_news": tabbed_news,
        "latest_pictures": latest_pictures,
        "genres_with_posts": genres_with_posts,
        "best_selling_videogames": best_selling_videogames,
    }

    return render(request, "home/home.html", context)
