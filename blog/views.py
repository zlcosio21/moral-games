from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from utils.citations import random_citation
from inventory.models import Videogame
from blog.models import Post, Comment


# Create your views here.
def blog(request):
    posts = Post.get_random_posts(10)

    context = {
        "posts": posts,
    }

    return render(request, "blog/blog.html", context)


def watch_post(request, id):
    post = Post.get(id=id)
    citation = random_citation()
    similar_posts = Post.get_random_posts(2)

    context = {
        "post": post,
        "citation": citation,
        "similar_posts": similar_posts
    }

    return render(request, "blog/blog_post.html", context)


@require_POST
def add_comment_to_post(request, id):
    comment_content = request.POST.get("comment_content")
    comment = Comment.create(request, comment_content)

    post = Post.get(id=id)
    post.add_comment(comment)

    return redirect("ver_post", id=post.id)


@require_POST
def add_comment_to_videogame(request, id):
    comment_content = request.POST.get("comment_content")
    comment = Comment.create(request, comment_content)

    videogame = Videogame.get(id=id)
    videogame.add_comment(comment)

    return redirect("ver_videojuego", id=videogame.id)
