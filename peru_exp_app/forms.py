from .models import Comment, Place
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
        model = Place
        fields = ('image', 'name', 'slug', 'region', 'cardinal_location', 'altitude', 'type_location', 'info', 'author', )
        prepopulated_fields = {'slug': 'name', }


class UpdatePlacesForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('image', 'name', 'slug', 'region', 'cardinal_location', 'altitude', 'type_location', 'info', 'author', )


class SearchPlacesForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name',)