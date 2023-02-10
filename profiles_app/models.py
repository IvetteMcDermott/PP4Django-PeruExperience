from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


# Create your models here.


class UserProfile(models.Model):
    traveller_type_options = [
                                ('Adventure', 'Adventure'),
                                ('Relaxed', 'Relaxed'),
                                ('Tourist', 'Tourist'),
                                ('Cultural', 'Cultural'),
                            ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    picture = CloudinaryField(default='placeholder', max_length=255, verbose_name='picture')
    bio = RichTextField(null=False, blank=False)
    traveller_type = models.CharField(max_length=50, choices=traveller_type_options)
    joined = models.DateField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)
