from turtle import title
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.title
   