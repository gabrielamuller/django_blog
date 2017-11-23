from django.conf.urls import url
from .views import post_list, add_post, edit_post, viewpost, whatever, delete_post, add_comment

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^posts/add/$', add_post, name='add_post'),
    url(r'^posts/edit/(.+)$', edit_post, name='edit_post'),
    url(r'^posts/delete/(.+)$', delete_post, name='delete_post'),
    url(r'^posts/comments/(.+)$', add_comment, name="add_comment"),
    url(r'^posts/(.+)$', viewpost, name='viewpost'),
    #url(r'^posts/(\d+)/comments/add$', add_comment, name="add_comment"),
    url(r'', whatever),
]