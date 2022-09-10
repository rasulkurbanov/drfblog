from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.contrib.auth.models import User

from .serializers import CommentSerializer, UserSerializer, PostSerializer
from .models import Post, Comment
from .permissions import IsOnwerOrReadOnly


# Create your views here.
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #user must be logged in to crate a new post, otherwise only can see posts list
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #to set the owner field to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #user can see a single post detail but cannot modify, user must be logged in and be owner of the post to modify
    permission_classes = [IsOnwerOrReadOnly]


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOnwerOrReadOnly]