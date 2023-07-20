from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile_images', default='profile_images/default.jpg')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return str(self.user)
