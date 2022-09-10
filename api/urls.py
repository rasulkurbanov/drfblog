from django.urls import path
from .views import UserList, UserDetail, PostList, PostDetail, CommentList, CommentDetail


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view(), name='comment-detail'),
]

