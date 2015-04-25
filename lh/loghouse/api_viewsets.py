from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.contenttypes.models import ContentType

from loghouse.models import (
        Post,
        Stream,
        Tag,
        )

from loghouse.serializers import (
        TagSerializer,
        StreamSerializer,
        PostSerializer,
        )

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




