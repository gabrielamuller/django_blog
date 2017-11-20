from django.conf.urls import url
from .views import post_list, add_post, edit_post, viewpost, whatever, delete_post

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^posts/(\d+)', viewpost, name='viewpost'),
    url(r'^posts/add/$', add_post, name='add_post'),
    url(r'^posts/edit/(\d+)$', edit_post, name='edit_post'),
    url(r'^posts/delete/(\d+)$', delete_post, name='delete_post'),
    url(r'', whatever),
]