'''When you're done, you should be able to visit
http://localhost:8000/latest/feed/
to see an RSS formatted list of your blog posts.
'''
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post
# from django.http import HttpResponse, HttpResponseRedirect, Http404


class PostFeed(Feed):
    title = "Latest Posts"
    link = "/latest/feed/"
    description = "RSS formatted feed of Posts"

    def items(self):
        published = Post.objects.exclude(published_date__exact=None)
        return published.order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
