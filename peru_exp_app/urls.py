from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('interests/', views.interests, name='interests'),
    path('adminpage/', views.AdminPage.as_view(), name='admin_page'),
    path('admin/', views.admin, name='admin'),
    path('searchpage/', views.search, name='search'),
    path('searchplace/', views.search_place, name='search_place'),
    path('home/coast/', views.Coast.as_view(), name='coast_places_display'),
    path('home/andes/', views.Andes.as_view(), name='andes_places_display'),
    path('home/jungle/', views.Jungle.as_view(), name='jungle_places_display'),
    path('<slug:slug>/', views.PlaceInformation.as_view(),
         name='place_information'),
    path('add_interest/<slug:slug>', views.add_interest, name='add_interest'),
    path('<slug:slug>/update/', views.place_update_view,
         name='edit_place_information'),
    path('<slug:slug>/delete/', views.place_delete_view,
         name='delete_place_information'),
    path('<slug:slug>/<int:pk>/update/', views.comment_update_view,
         name="comment_update"),
    path('<slug:slug>/<int:pk>/delete/', views.comment_delete_view,
         name="comment_delete"),
]
