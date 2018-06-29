from django.urls import path, include
from django.conf.urls import url
from posts.views import list_posts, AddPost
from posts.api import urls as api_urls


urlpatterns = [
    path(r'api/', include(api_urls)),
    path(r'list/', list_posts, name='list_posts'),
    url(
        r'^search/(?P<tagname>\w+)$',
        list_posts,
        name='list_posts_by_tag'
    ),
    path(r'add/', AddPost.as_view(), name='add_post'),
]
