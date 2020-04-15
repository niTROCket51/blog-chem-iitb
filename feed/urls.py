"""URL declarations for the 'feed' app for the site."""

from django.urls import path
from . import views

urlpatterns = [
    # ex: /feed/
    path('', views.PostList.as_view(), name='home'),
    # ex: /feed/search/
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    # ex: /feed/aboutus/
    path('aboutus/', views.AboutUsView.as_view(), name='about_us'),
    # ex: /feed/coursereview/
    path('coursereview/', views.CourseReviewView.as_view(), name='coursereview_index'),
    # ex: /feed/post-title/
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
