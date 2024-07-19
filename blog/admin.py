from .models import Post, Comment
from django.contrib import admin


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
