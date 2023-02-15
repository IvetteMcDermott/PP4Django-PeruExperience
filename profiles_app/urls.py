from django.urls import path
from . import views


app_name = 'profiles_app'
urlpatterns = [
    path('myprofile/', views.my_profile, name='my_profile'),
    ]
