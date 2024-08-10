from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('authorization', views.authorization, name='authorization'),
    path('registration', views.registration, name='registration'),
    path('article', views.article, name='article'),
    path('addarticle', views.addarticle, name='add article'),
    path('editarticle', views.editarticle, name='edit article'),
]
