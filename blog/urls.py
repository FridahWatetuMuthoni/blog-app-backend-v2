from django.urls import path
from .views import PostDetail, PostList, CategoryListView

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('<str:pk>/', PostDetail.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]