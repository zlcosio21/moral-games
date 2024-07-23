from moral_games.base_models import Models
from django.db.models import Q, Value
from django.db import models
import random


# Create your models here.
class Platform(Models):
    name = models.CharField(unique=True, max_length=50, null=False)

    @classmethod
    def get(cls, name):
        if name is None or not cls.exist(name):
            return cls.get_random_platform()

        return cls.objects.get(name__iexact=name)

    @classmethod
    def get_all_platforms(cls):
        return cls.objects.all().order_by("?")

    @classmethod
    def get_random_platform(cls):
        return cls.objects.all().order_by("?").first()

    @classmethod
    def exist(cls, name):
        return cls.objects.filter(name__iexact=name).exists()

    def __str__(self):
        return self.name


class Genre(Models):
    name = models.CharField(unique=True, max_length=50, null=False)

    @classmethod
    def get(cls, name):
        if name is None:
            return cls.get_random_genre()

        return cls.objects.get(name=name)

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_all_genres(cls, limit=0):
        if limit > 0:
            return cls.objects.all().order_by("?")[:limit]

        return cls.objects.all().order_by("?")

    @classmethod
    def get_random_genre(cls):
        return cls.objects.all().order_by("?").first()

    def get_random_picture_of_the_genre(self):
        return Videogame.get_pictures_by_genre(self)

    @staticmethod
    def get_all_pictures(pictures_videogames, pictures_posts):
        all_pictures = list(pictures_videogames.union(pictures_posts))

        return random.sample(all_pictures, len(all_pictures))

    def __str__(self):
        return self.name


class Videogame(Models):
    name = models.CharField(unique=True, max_length=50, null=False)
    image = models.ImageField(upload_to="store", null=False)
    price = models.PositiveIntegerField(null=False)
    quantity = models.PositiveIntegerField(null=False)
    genre = models.ManyToManyField(Genre)
    platform = models.ManyToManyField(Platform)
    description = models.CharField(max_length=485, null=True)
    comments = models.ManyToManyField("blog.comment", blank=True)

    def update_stock(self, quantity):
        self.quantity -= int(quantity)
        self.save()

    def get_random_star(self):
        return random.choice(["fa fa-star", "far fa-star"])

    def get_description_featured_game(self):
        if len(self.description) > 165:
            return f"{self.description[:165]}..."

        return self.description

    def get_count_of_comments(self):
        return len(self.comments.all())

    def get_comments_videogame(self):
        return self.comments.all()

    def add_comment(self, comment):
        self.comments.add(comment)

    @classmethod
    def get_pictures_by_genre(cls, genre, limit=1, all=False):
        if all:
            query = cls.objects.filter(genre=genre).values("name", "image", "description")
            query = query.annotate(type=Value("videogame"))

            return query

        if limit > 1:
            return cls.objects.filter(genre=genre).values("image").order_by("?")[:limit]

        return cls.objects.filter(genre=genre).values("image").order_by("?").first()

    @classmethod
    def get(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_random_videogames(cls, limit=1):
        if limit > 1:
            return cls.objects.all().order_by("?")[:limit]

        return cls.objects.all().order_by("?").first()

    @classmethod
    def get_random_name_videogames(cls, limit=1):
        if limit > 1:
            return cls.objects.all().values("name").order_by("?")[:limit]

        return cls.objects.all().values("name").order_by("?").first()

    @classmethod
    def get_videogames_by_genre(cls, genre, limit=1):
        if limit > 1:
            return cls.objects.filter(genre=genre).order_by("?")[:limit]

        return cls.objects.filter(genre=genre).order_by("?").first()

    @classmethod
    def get_videogames_by_platform(cls, platform, limit=1):
        if limit > 1:
            return cls.objects.filter(platform=platform).order_by("?")[:limit]

        return cls.objects.filter(platform=platform).order_by("?").first()

    @classmethod
    def get_latest_pictures(cls):
        query = cls.objects.all().values("name", "image", "description", "created")
        query = query.annotate(type=Value("videogame"))

        return query

    @classmethod
    def search(cls, search):

        videogames = cls.objects.filter(
            Q(name__icontains=search)
            | Q(platform__name__icontains=search)
            | Q(genre__name__icontains=search)
        ).distinct()

        return videogames

    @classmethod
    def search_by_price(cls, search):
        min_price, max_price = search.split(",")

        videogames = cls.objects.filter(
            Q(price__gte=min_price) & Q(price__lte=max_price)
        ).distinct()

        return videogames

    @classmethod
    def update_stock_in_cart(cls, cart):
        for item in cart:
            videogame = cls.get(id=item.videogame.id)
            videogame.update_stock(item.quantity)

    def __str__(self):
        genres = ", ".join([genre.name for genre in self.genre.all()])
        platforms = ", ".join([platform.name for platform in self.platform.all()])

        return f"{self.name} - Precio {self.price} - Cantidad {self.quantity} - Genero(s) {genres} - Plataforma(s) {platforms}"
