"""Public interface which shows the latest feed for the blog."""

from django.views import generic
from django.db.models import Q
from .models import Post, CourseReviewData

class PostList(generic.ListView):
    """Views showing blog index."""
    queryset = Post.objects.order_by('-published_date')
    template_name = 'feed/index.html'
    paginate_by = 5
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    """Views showing full content of selected Post"""
    model = Post
    template_name = 'feed/post_detail.html'

class SearchResultsView(generic.ListView):
    """Views showing results to search queries."""
    model = Post
    template_name = 'feed/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list

class VisionView(generic.ListView):
    """Views for Vision page"""
    model = Post
    template_name = 'feed/vision.html'

class CourseReviewView(generic.ListView):
    """Views for Course Reviews index page."""
    template_name = 'feed/coursereview_index.html'
    context_object_name = 'course_list'
    queryset = CourseReviewData.objects.order_by('course')

    # pylint: disable=W0221
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sem"] = ['first', 'second', 'third', 'fourth', 'fifth',
                          'sixth', 'seventh', 'eighth', 'electives']
        return context

class CourseReview(generic.DetailView):
    """Views showing details of Course Review."""
    model = CourseReviewData
    template_name = 'feed/coursereview.html'
