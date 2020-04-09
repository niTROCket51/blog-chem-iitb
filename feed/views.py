"""Public interface which shows the latest feed for the blog."""

from django.views import generic
from django.db.models import Q
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-published_date')
    template_name = 'feed/index.html'
    paginate_by = 5
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'feed/post_detail.html'

class SearchResultsView(generic.ListView):
    """Class to be used for search queries"""
    model = Post
    template_name = 'feed/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list
