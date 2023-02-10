from django.urls import path
from . import views


app_name = 'profiles_app'
urlpatterns = [
    path('profile/', views.MyProfile, name='my_profile')
    ]
