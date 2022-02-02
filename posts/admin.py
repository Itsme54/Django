from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    admin.site.register(Post)
