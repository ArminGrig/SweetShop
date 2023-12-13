from django.urls import path
from . import views
from. views import *

urlpatterns = [
    path('', index, name='index'),
    path('cakes/', cakes, name='cakes'),
    path('category/<int:category_id>/',get_category, name='category'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),



]
