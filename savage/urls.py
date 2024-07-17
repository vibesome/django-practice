from django.urls import path
from savage.views import*

urlpatterns = [
path('', home),
path('login', login),
path('signup', signup, name='signup'),
]