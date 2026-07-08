from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:tag_id>/', views.posts_by_tag, name='posts_by_tag'),
]