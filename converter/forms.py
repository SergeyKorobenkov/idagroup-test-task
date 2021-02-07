import requests
from urllib.request import urlopen
from urllib.error import HTTPError

from django import forms
from django.core.exceptions import ValidationError
from .models import BaseImage
from .utils import url_validation


class ImageForm(forms.ModelForm):
    '''
    Image publication form
    '''
    class Meta:
        model = BaseImage
        fields = ('url', 'image',)

    def clean(self):
        '''
        Check that data only in one field
        '''
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        image = cleaned_data.get('image')

        if (url and image) or (not url and not image):
            raise ValidationError(
        'Заполните хотя бы одно поле'
        'Проверьте работоспособность ссылки')

        return cleaned_data

    def clean_url(self):
        '''
        Url-validation
        '''
        url = self.cleaned_data.get('url')

        if url == None or url == '':
            return url

        response = requests.get(url)
        if response.status_code != 200:
            raise ValidationError('Проверьте работоспособность ссылки или попробуйте другую')

        if not url_validation(url):
            raise ValidationError('Не надо сюда пихать что то помимо изображений, пожалуйста',)
        
        return url


class ResizeForm(forms.Form):
    '''
    Form for resize images
    '''
    width = forms.IntegerField(
        max_value=100000, 
        min_value=1, 
        label='Ширина', 
        required=False)
    height = forms.IntegerField(
        max_value=100000, 
        min_value=1, 
        label='Высота', 
        required=False)

    def clean(self):
        ''' 
        Check that data in the one field minimum
        '''
        cleaned_data = self.cleaned_data
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')

        if width is None and height is None:
            raise ValidationError('Пожалуйста, заполните хотя бы одно поле :-)')
        
        return cleaned_data








        
