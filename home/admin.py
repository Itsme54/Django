from django.contrib import admin

# Register your models here.
from django.contrib import admin
from home.models import Profile


class PostAdmin(admin.ModelAdmin):
    #admin.site.register(uploads)

    admin.site.register(Profile)
