from django.db import models

# Create your models here
from django.conf import settings
from django.utils import timezone
import datetime


class driverPost(models.Model):

    class Post(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('drat', 'Drat'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=225)
    text = models.TextField(null=False)
    image = models.ImageField(blank=True)
    price = models.IntegerField()
    daystart = models.DateTimeField()
    slug = models.SlugField(max_length=225, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worktour'
    )
    status = models.CharField(
        max_length=50, choices=options, default=' published')
    objects = models.Manager()
    Post = Post()


class Meta:
    ok = ('push')


def __str__(self):
    return self.title
