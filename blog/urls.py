# from django.conf.urls import url
from django.urls import path, re_path

from . import views
app_name = 'post'
urlpatterns = [
    path('', views.list_post, name='index'),
    path('read-post/', views.read_post),
    path('category/<str:slug>/', views.post_category, name='category'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detail_post, name='detail'),
]