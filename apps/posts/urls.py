from django.urls import path
from .views import index, posts_list, post_detail, post_new, category_new, about

urlpatterns = [
    path('', index, name='index'),
    path('posts/<int:pk>/', posts_list, name='posts'),
    path('posts/post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('posts/post_add', post_new, name='post_add'),
    path('posts/category_add', category_new, name='category_add'),
    path('posts/about', about, name='about'),
]