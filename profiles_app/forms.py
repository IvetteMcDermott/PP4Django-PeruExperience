from .models import UserProfile
from django import forms
from django.forms import fields, ModelForm
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class UpProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = UserProfile
        fields = ('user_name', 'location', 'picture', 'bio', 'traveller_type', )

