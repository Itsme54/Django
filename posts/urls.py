from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.post_index, name="post_index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]
