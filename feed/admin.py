"""Admin page for site managers."""

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
