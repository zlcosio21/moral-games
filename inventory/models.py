from moral_games.base_models import Models
from django.db.models import Q
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
    def get_all_genres(cls):
        return cls.objects.all().order_by("?")

    @classmethod
    def get_random_genre(cls):
        return cls.objects.all().order_by("?").first()

    def __str__(self):
        return self.name
