from django import forms
from django.core import validators
from gallery_iit.models import Image
from gallery_iit.models import Video

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image', )


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video', )

