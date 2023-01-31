from .models import Comment, PlacesList
from django import forms
from django.forms import fields, ModelForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPlacesForm(forms.ModelForm):
    class Meta:
        model = PlacesList
        fields = ('place_image_src', 'place', 'slug', 'region', 'location', 'altitude', 'type_location', 'info', 'author', )
        prepopulated_fields = {'slug': "place", }


class UpdatePlacesForm(forms.ModelForm):
    class Meta:
        model = PlacesList
        fields = ('place_image_src', 'place', 'slug', 'region', 'location', 'altitude', 'type_location', 'info', 'author', )


class SearchPlacesForm(forms.ModelForm):
    class Meta:
        model = PlacesList
        fields = ('place',)