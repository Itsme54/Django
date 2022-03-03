from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
     path("", include("home.urls")),
     path("createpost/",views.createpost_view, name="createpost_view"),
     #path(" ", views.post_index, name="post_index"),
     # path('post_index/', views.post_index, name="post_index"),
     # path('<int:pk>/', views.post_detail, name="post_detail"),
     path("posts/", include("posts.urls")),
     path("product/", include("product.urls")),

]
