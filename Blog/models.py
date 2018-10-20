from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.new()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
