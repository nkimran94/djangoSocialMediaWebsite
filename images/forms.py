from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','url','description')
        widgets = {
            'url': forms.HiddenInput,
        }
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extention = url.rsplit('.',1)[1].lower()
        if extention not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extension.')
        return url
    #------------------------------
    #Overriding the save() method of a ModelForm
    def save(self,force_insert=False,force_update=False,commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.',1)[1].lower()
        image_name = f'{name}.{extension}'
        #download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name,ContentFile(response.read()),save=False)
        if commit:
            image.save()
        return image