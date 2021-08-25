from django.urls import path
from .views import *

app_name = 'blogs'

urlpatterns = [
    path('',index,name='index'),
    path('posts/<post_id>',post,name='post'),
    path('posts/create/',create,name='create'),
    path('posts/update/<post_id>',update,name='update'),
    path('posts/delete/<post_id>',delete,name='delete'),
]