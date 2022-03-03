from django.contrib.auth import admin
from django.urls import path
from . import views
from .views import cookie_session, cookie_delete
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('reset/', views.reset, name='reset'),
    path('validate_user/', views.validate_user, name='validate_user'),
    path('delete_user/', views.delete_user_view, name='delete_user_view'),
    path('profile/', views.profile, name='profile'),
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),
    #path('createpost/',views.createpost_view, name="create_post"),
    # path("", views.post_index, name="post_index"),
    # path("<int:pk>/", views.post_detail, name="post_detail"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
