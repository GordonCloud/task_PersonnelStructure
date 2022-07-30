from django.urls import path

from . import views

urlpatterns = [
    path('', views.page, name='mainpage'),
    path('search/', views.searchpage, name='searchpage'),
    path('search/new/', views.post_searchform, name='post_searchform'),
]
