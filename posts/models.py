from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):

    name = models.CharField(max_length=25)


class Post(models.Model):

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
