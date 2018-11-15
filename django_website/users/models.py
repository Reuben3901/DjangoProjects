from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class ProfilePictures(models.Model):
    image = models.ImageField(upload_to='profile_pics', null=True, default='profile_pics/default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} {self.image}'
