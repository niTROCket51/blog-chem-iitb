"""Public interface which shows the latest feed for the blog."""

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
    