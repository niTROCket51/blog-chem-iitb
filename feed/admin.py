"""Admin page for site managers."""

from django.contrib import admin
from .models import Post, Course, CourseReviewData

class PostAdmin(admin.ModelAdmin):
    """Class representing Post model in admin display."""
    list_display = ['title', 'author', 'published_date']
    search_fields = ['title']

class CourseAdmin(admin.ModelAdmin):
    """Class representing Course model in admin display."""
    list_display = ['code', 'name', 'semester']

class CourseReviewDataAdmin(admin.ModelAdmin):
    """Class representing CourseReviewData model in admin display."""
    list_display = ['submitter', 'course', 'session']

admin.site.register(Post, PostAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseReviewData, CourseReviewDataAdmin)
