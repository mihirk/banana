from django.conf.urls import patterns, include, url
from views import BlogView
from django.contrib import admin
admin.autodiscover()

blogView = BlogView()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'banana.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', blogView.blog_post_view),
    url(r'^admin/', include(admin.site.urls)),
)
