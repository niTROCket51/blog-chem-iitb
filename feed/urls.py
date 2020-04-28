"""URL declarations for the 'feed' app for the site."""

from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.PostList.as_view(), name='home'),
    # ex: /search/
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    # ex: /vision/
    path('vision/', views.VisionView.as_view(), name='vision'),
    # ex: /coursereview/
    path('coursereview/', views.CourseReviewView.as_view(), name='coursereview_index'),
    # ex: /post-title/
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # ex: review/course-code/
    path('review/<slug:slug>/', views.CourseReview.as_view(), name='coursereview'),
]
