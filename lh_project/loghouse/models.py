from django.db import models
from django.contrib.auth.models import User

class Dated(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Post(Dated):
    #creator = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

class Stream(Dated):
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    #creator = models.ForeignKey(User)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

"""
Post (Information about the post such as tags, title, summary)
    date_added
    date_edited
    creator
    title - optional
    tags - optional, comma-separated list
    body - optional, probably markdown
    _attachments - optional
Stream (a category underwhich posts are created, a simple way to separate them.)
    name
    description - optional
    creator
    date_added
    date_edited
Tag (a small string that can be used to organize Posts)
    slug
    creator
    count
    _posts
    date_added
    date_edited
"""

