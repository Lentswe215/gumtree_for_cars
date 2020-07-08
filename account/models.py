from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Dealership = models.CharField(max_length=180)
    profile_pic = models.ImageField(default='noimage.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} profile'

# Create your models here.
