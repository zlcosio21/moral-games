from inventory.models import Platform, Genre, Videogame
from django.contrib import admin


# Register your models here.
class PlatformAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class VideogameAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Platform, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Videogame, VideogameAdmin)
