from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()
from groups.models import Group


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    text_html = models.TextField(editable=False, default='')
    published_date = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.text_html = misaka.html(self.text)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={
            "username": self.user.username,
            "pk": self.pk})

    class Meta():
        ordering = ['-published_date']
        unique_together = ['user', 'text']

    def __str__(self):
        return self.text
