from django.urls import path
from .views import  home, create_post

app_name = 'community'  #  'community' namespace
urlpatterns = [
    path('home/', home, name='home'),
    path('post/create/', create_post, name='create_post'),
]
