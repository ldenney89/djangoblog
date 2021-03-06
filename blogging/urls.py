from django.urls import path
from blogging.views import list_view, detail_view, add_post, add_category
from blogging.feeds import PostFeed


urlpatterns = [
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', list_view, name="blog_index"),
    path('add/post', add_post, name="blog_add_post"),
    path('add/category', add_category, name="blog_add_category"),
    path('latest/feed', PostFeed()),
]
