from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    #used to return the username of the owner addition to its id
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment-detail')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'posts', 'comments']



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']