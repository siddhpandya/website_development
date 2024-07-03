from django import forms
from .models import MediaUpload

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaUpload
        fields = ['video', 'ppt', 'latitude', 'longitude']
