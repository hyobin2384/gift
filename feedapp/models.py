from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Main


class Feed(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='feed', null=True)
    image = models.ImageField(upload_to='main/', null=False)
    profile_image = models.ImageField(upload_to='profile/', null=False)
    like_count = models.IntegerField()
    Main.objects.all()