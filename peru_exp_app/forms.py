from .models import Comment, Place
from django import forms
from django.forms import fields, ModelForm
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        fields = ('body',)


class UpdateCommentForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        fields = ('body',)


class AddPlacesForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Place
        fields = ('image', 'name', 'region', 'cardinal_location', 'altitude', 'type_location', 'info', 'author', )
        prepopulated_fields = {'slug': 'name', }


class UpdatePlacesForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Place
        fields = ('image', 'name', 'region', 'cardinal_location', 'altitude', 'type_location', 'info', 'author', )


class SearchPlacesForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name',)