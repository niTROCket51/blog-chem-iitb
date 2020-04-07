"""Public interface which shows the latest feed for the blog."""

from django.views import generic
from .models import Post
from django.template import loader

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-published_date')
    template_name = 'feed/index.html'
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'feed/post_detail.html'
