from django.contrib import admin
from models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'timestamp', 'content',)
    list_display = ("title", "author", "timestamp",)
    list_filter = ("title", "timestamp",)

admin.site.register(BlogPost, BlogPostAdmin)