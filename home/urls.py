from django.contrib.auth import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="Homepage"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")


]
