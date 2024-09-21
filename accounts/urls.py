from django.urls import path
from django.contrib.auth import views as auth_views
from .views import welcome, login,logout, register, profile, user_info

app_name = 'accounts'  #  'accounts' namespace
urlpatterns = [
    path('', welcome, name = 'welcome'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('user_info/', user_info, name='user_info'),
    path('profile/', profile, name='profile'),
]
