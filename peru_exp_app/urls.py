from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('profile/', views.profile, name='profile'),
    path('addplace/', views.AddPlace, name='add_place'),
    path('home/coast/', views.Coast.as_view(), name='coast_places_display'),
    path('home/andes/', views.Andes.as_view(), name='andes_places_display'),
    path('home/jungle/', views.Jungle.as_view(), name='jungle_places_display'),
    path('<slug:slug>/', views.PlaceInformation.as_view(), name='place_information'),
    path('<slug:slug>/<int:pk>/update/', views.comment_update_view, name="comment_update"),
    path('<slug:slug>/<int:pk>/delete/', views.comment_delete_view, name="comment_delete"),
]
