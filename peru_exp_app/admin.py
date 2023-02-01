from django.contrib import admin
from .models import Place, Comment, UserProfile

# Register your models here.


# @admin.register(Place)
# class PlacesItems(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
#     list_filter = ('region', 'type_location')
#     search_fields = ['region', 'type_location', 'name']
#     list_display = ('name', 'type_location', 'cardinal_location', 'info', 'region', 'altitude', 'author', 'date_created', 'date_updated')


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'author', 'date_created', 'date_updated')
#     list_filter = ('author', 'name')
#     search_fields = ['author', 'name']


# @admin.register(UserProfile)
# class UserProfile(admin.ModelAdmin):
#     list_display = ['user', 'user_name']
#     list_filter = ('user_name', 'interests')
#     search_fields = ['user_name']
