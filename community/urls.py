from django.urls import path
from .views import  posts_list, create_post

app_name = 'community'  #  'community' namespace
urlpatterns = [
    path('home/', posts_list, name='home'),
    path('post/create/', create_post, name='create_post'),
]
