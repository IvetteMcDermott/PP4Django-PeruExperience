from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.


class PlacesList(models.Model):
    place_image_src = CloudinaryField('image', default='placeholder')
    place = models.CharField(max_length=60, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=60, null=False, unique=True)
    region = models.CharField(max_length=15, null=False, blank=False)
    location = models.CharField(max_length=20, null=False, blank=False)
    altitude = models.IntegerField(null=False, blank=False)
    type_location = models.CharField(max_length=20, null=False, blank=False)
    info = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    date_updated = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.place


class Comment(models.Model):
    place = models.ForeignKey(PlacesList, related_name="comments", null=False, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    author = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'Comment {self.body} by {self.author}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    interests = models.ManyToManyField(PlacesList)

    def __str__(self):
        return self.user_name
