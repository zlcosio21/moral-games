from blog.models import Post


def posts_footer(request):
    posts = Post.get_latest_posts(2)

    return {"posts_footer":posts}