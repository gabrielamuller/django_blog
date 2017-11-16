from django.conf.urls import url
from .views import post_list, add_post, edit_post, viewpost

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^posts/(\d+)', viewpost, name='viewpost'),
    url(r'add$', add_post, name='add_post'),
    url(r'^edit/(\d+)$', edit_post, name='edit_post'),
]