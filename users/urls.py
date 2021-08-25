from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('',index,name='index'),
    path('register/',register,name='register'),
]
