from django.urls import path

from . import views

urlpatterns = [
    path('', views.page, name='mainpage'),
    path('search/', views.searchpage, name='searchpage'),
]
