from django.shortcuts import render
from .models import UserProfile
from django.views import generic, View


# Create your views here.

def MyProfile(request):
    """ VIEW FOR PROFILE PAGE """
    return render(request, 'user_profile.html')

