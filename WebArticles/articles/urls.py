from django.urls import path, include
from . import views, admin

urlpatterns = [
    path('', views.main, name='main'),
    path(r'^article/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article-detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.registration, name='registration'),

    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:pk>', views.edit_article, name='edit_article'),
    path('delete_article/<int:pk>', views.delete_article, name='edit_article'),
]

