"""Model for the the 'feed' app.

The module models.py contains the essesntial field and
behaviour of data stored for the app named feed.

"""

from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    """The class that defines Post object for the blog."""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        """The method responsible for publishing a post."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """String representation of a Post object."""
        return self.title
