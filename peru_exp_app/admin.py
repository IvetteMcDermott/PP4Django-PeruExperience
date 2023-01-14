from django.contrib import admin
from .models import PlacesList, Comment, UserProfile

# Register your models here.


@admin.register(PlacesList)
class PlacesItems(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('place',)}
    list_filter = ('region', 'type_location')
    search_fields = ['region', 'type_location', 'place']
    list_display = ('place', 'type_location', 'location', 'info', 'region', 'altitude', 'author', 'date_created', 'date_updated')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('place', 'body', 'date_created', 'date_updated')
    list_filter = ('author', 'place')
    search_fields = ['author', 'place']


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user', 'user_name']
    list_filter = ('user_name', 'interests')
    search_fields = ['user_name']
