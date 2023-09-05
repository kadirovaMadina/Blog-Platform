from rest_framework import serializers
from ..models import Post
from users.serializers  import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', "title", "description", "photo", "user", "date")


class PostCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = ("title", "description", "photo", "user", "date")


class PostEditSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Post
    fields = ("title", "description", "photo", "user","date")