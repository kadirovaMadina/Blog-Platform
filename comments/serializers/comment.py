from rest_framework import serializers
from ..models import Comment
from users.serializers import UserSerializer
from posts.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):

  user = UserSerializer()
  post = PostSerializer()

  class Meta:
    model = Comment
    fields = ('id', "user", "post", "text", "date")


class CommentCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ("user", "post", "text", "date")


class CommentEditSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Comment
    fields = ("user", "post", "text", "date")