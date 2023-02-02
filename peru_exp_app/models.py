from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.


class Place(models.Model):
    type_location_options = [
                        ('Beach', 'Beach'),
                        ('Nature', 'Nature'),
                        ('Arqueologic', 'Arqueologic'),
                        ('Cultural', 'Cultural'),]
    region_options = [
                    ('Coast', 'Coast'),
                    ('The Andes', 'The Andes'),
                    ('Jungle', 'Jungle'),]
    cardinal_location_options = [
                                ('North', 'North'),
                                ('Center', 'Center'),
                                ('South', 'South'),]
    image = CloudinaryField(default='placeholder', max_length=255, verbose_name='image')
    name = models.CharField(max_length=60, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=60, null=False, unique=True)
    region = models.CharField(max_length=15, choices=region_options, null=False, blank=False)
    cardinal_location = models.CharField(max_length=20, choices=cardinal_location_options, null=False, blank=False)
    altitude = models.IntegerField(null=False, blank=False)
    type_location = models.CharField(max_length=20, choices=type_location_options, null=False, blank=False)
    info = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, null=False, blank=False)
    date_updated = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    place = models.ForeignKey(Place, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'Comment {self.body} by {self.author}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(Place, related_name='interest', blank='True')

    def __str__(self):
        return str(self.user)
