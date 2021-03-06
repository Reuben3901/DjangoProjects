from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #reverse url returns a stings, url redirect doesn't
        # The promary key will be the post with the specific pk
        return reverse('post-detail', kwargs={'pk':self.pk})
