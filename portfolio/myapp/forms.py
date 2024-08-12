from django import forms
from .models import Post

class upload_media(forms.Form):
    video = forms.FileField(required=True)
    link = forms.URLField(required=True)
    image = forms.ImageField(required=True)