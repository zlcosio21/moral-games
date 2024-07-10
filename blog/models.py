from django.db.models import OuterRef, Subquery
from django.contrib.auth.models import User
from moral_games.base_models import Models
from django.db.models import Value
from inventory.models import Genre
from django.db import models


class Post(Models):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog", null=False, blank=False)
    content = models.CharField(max_length=500, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


    @classmethod
    def get(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_random_posts(cls, limit=1):
        if limit > 1:
            return cls.objects.all().order_by("?")[:limit]

        return cls.objects.all().order_by("?").first()

    @classmethod
    def get_all_genres_post(cls):
        return cls.objects.values("genre__name").order_by("genre__name").distinct()

    @classmethod
    def get_tabbed_news(cls):
        random_post_ids = (cls.objects.filter(genre=OuterRef("genre")).order_by("?").values("id")[:1])

        return cls.objects.filter(id__in=Subquery(random_post_ids)).order_by("genre__name")

    @classmethod
    def get_pictures_by_genre(cls, genre, limit=1, all=False):
        if all:
            query = cls.objects.filter(genre=genre).values("title", "image", "content")
            query = query.annotate(type=Value("post"))

            return query

        if limit > 1:
            return cls.objects.filter(genre=genre).values("image").order_by("?")[:limit]

        return cls.objects.filter(genre=genre).values("image").order_by("?").first()

    @classmethod
    def get_latest_pictures(cls):
        query = cls.objects.all().values("title", "image", "content", "created")
        query = query.annotate(type=Value("post"))

        return query

    @classmethod
    def get_latest_posts(cls, limit=1):
        if limit > 1:
            return cls.objects.all().order_by("-created")[:limit]

        return cls.objects.all().order_by("-created").first()

    def add_comment(self, comment):
        self.comments.add(comment)

    def get_count_of_comments(self):
        return len(self.comments.all())

    def get_content_main_latest_news(self):
        if len(self.content) > 150:
            return f"{self.content[:150]}..."

        return self.content

    def get_content_latest_posts(self):
        if len(self.content) > 140:
            return f"{self.content[:140]}..."

        return self.content

    def get_content_posts_list(self):
        if len(self.content) > 160:
            return f"{self.content[:160]}..."

        return self.content

    def get_color_genre(self):

        COLORS = {
            "accion": 1,
            "aventura": 2,
            "estrategia": 3,
            "indie": 4,
            "mundo abierto": 5,
            "survival horror": 6,
        }

        genre_name = self.genre.name.lower()

        return COLORS[genre_name] if genre_name in COLORS else 2

    def __str__(self):
        return self.title
