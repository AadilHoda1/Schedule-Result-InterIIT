from __future__ import unicode_literals
from django.db import models
# from embed_video.fields import EmbedVideoField


class Image(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True)
    video = models.URLField(max_length=100)

    def __str__(self):
        return str(self.title)





