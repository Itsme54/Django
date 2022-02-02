from django.contrib import admin

# Register your models here.
from django.contrib import admin
from home.models import uploads


class PostAdmin(admin.ModelAdmin):
    admin.site.register(uploads)
