from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('createpost/', views.createpost_view, name="createpost_view"),
    path(" ", views.post_index, name="post_index"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]
