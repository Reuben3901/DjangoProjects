from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'



    # Resizing images and Overwirting the save model
    def save(self):

        # Delete old Profile Image
        try:
            this = Profile.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        # Overwrites the save.
        # Grabs the the parent saved image and resizes it
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ProfilePictures(models.Model):
    image = models.ImageField(upload_to='profile_pics', null=True, default='profile_pics/default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} {self.image}'
