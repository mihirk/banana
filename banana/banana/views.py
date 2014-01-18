from django.shortcuts import render
from models import BlogPost

class BlogView:
    def blog_post_view(self, request, template="index.html"):
        return render(request, template, {"blog_posts": BlogPost.objects.all()})

