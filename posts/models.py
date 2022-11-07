from django.db import models
import cloudinary
import cloudinary.uploader
import cloudinary.api


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=False, null=False, max_length=140, db_index=True,
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    image = CloudinaryField(
        'image', blank=True, null=True, db_index=True
    )
    likecount = models.IntegerField(
        'Like', default=0, null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
