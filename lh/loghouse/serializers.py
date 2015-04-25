from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User

from loghouse.models import (
        Post,
        Tag,
        Stream
        )

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag

class StreamSerializer(ModelSerializer):
    class Meta:
        model = Stream

class TagFieldSerialzier(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('slug')

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post

