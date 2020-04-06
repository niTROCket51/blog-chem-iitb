"""URL declarations for the 'feed' app for the site."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
