"""URL declarations for the 'feed' app for the site."""

from django.urls import path
from . import views

urlpatterns = [
    # ex: /feed/
    path('', views.PostList.as_view(), name='home'),
    # ex: /feed/search/
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    # ex: /feed/my-post/
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
