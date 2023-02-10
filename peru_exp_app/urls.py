from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('interests/', views.interests, name='interests'),
    path('adminpage/', views.AdminPage.as_view(), name='admin_page'),
    path('admin/', views.admin, name='admin'),
    path('searchplace/', views.SearchResults, name='search_place'),
    path('home/coast/', views.Coast.as_view(), name='coast_places_display'),
    path('home/coast/arqueologic', views.Coast.as_view(), name='arqueologic_coast_places_display'),
    path('home/coast/beach', views.BeachCoast.as_view(), name='beach_coast_places_display'),
    path('home/coast/nature', views.NatureCoast.as_view(), name='nature_coast_places_display'),
    path('home/coast/cultural', views.CulturalCoast.as_view(), name='cultural_coast_places_display'),
    path('home/andes/', views.Andes.as_view(), name='andes_places_display'),
    path('home/andes/nature', views.NatureAndes.as_view(), name='nature_andes_places_display'),
    path('home/andes/arqueologic', views.ArqueologicAndes.as_view(), name='arqueologic_andes_places_display'),
    path('home/andes/cultural', views.CulturalAndes.as_view(), name='cultural_andes_places_display'),
    path('home/jungle/', views.Jungle.as_view(), name='jungle_places_display'),
    path('home/jungle/nature', views.NatureJungle.as_view(), name='nature_jungle_places_display'),
    path('home/jungle/arqueologic', views.ArqueologicJungle.as_view(), name='arqueologic_jungle_places_display'),
    path('home/jungle/cultural/', views.CulturalJungle.as_view(), name='cultural_jungle_places_display'),
    path('<slug:slug>/', views.PlaceInformation.as_view(), name='place_information'),
    path('add_interest/<slug:slug>', views.add_interest, name='add_interest'),
    path('<slug:slug>/update/', views.place_update_view, name='edit_place_information'),
    path('<slug:slug>/delete/', views.place_delete_view, name='delete_place_information'),
    path('<slug:slug>/<int:pk>/update/', views.comment_update_view, name="comment_update"),
    path('<slug:slug>/<int:pk>/delete/', views.comment_delete_view, name="comment_delete"),
]
