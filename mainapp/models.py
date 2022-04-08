from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from profileapp.models import Profile
from projectapp.models import Project


class Main(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='main', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='main', null=True)

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='main', null=True)

    title = models.CharField(max_length=200, null=True)

    image = models.ImageField(upload_to='main/', null=False)

    content = models.CharField(max_length=300, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)