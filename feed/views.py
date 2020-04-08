"""Public interface which shows the latest feed for the blog."""

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-published_date')
    template_name = 'feed/index.html'
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'feed/post_detail.html'

class SearchResultsView(generic.ListView):
    """Class meant to be used for search queries"""
    model = Post
    template_name = 'feed/search_results.html'
