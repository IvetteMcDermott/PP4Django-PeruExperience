from django.urls import path
from . import views
from .views import landing_page, Coast, Andes, Jungle


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('coast/', views.Coast.as_view(), name='coast_places_display'),
    path('andes/', views.Andes.as_view(), name='andes_places_display'),
    path('jungle/', views.Jungle.as_view(), name='jungle_places_display'),
    path('<slug:slug>/', views.PlaceInformation.as_view(), name='place_information')
]