from django.db import models
from django.contrib.auth.models import User

class Dated(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Stream(Dated):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return "Stream:{}:{}".format(self.date_added.strftime("%Y-%m-%d"), self.name)

class Post(Dated):
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    stream = models.ForeignKey(Stream, blank=True, null=True)
    def __str__(self):
        return "Post:{}:{}".format(self.date_added.strftime("%Y-%m-%d"), self.title)

class Tag(Dated):
    slug = models.SlugField()
    creator = models.ForeignKey(User)
    count = models.IntegerField(default=0)
    posts = models.ManyToManyField(Post, blank=True, related_name='tags')

