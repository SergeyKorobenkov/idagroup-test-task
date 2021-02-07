import os
from urllib.request import urlretrieve

from django.db import models
from django.core.files import File



class BaseImage(models.Model):
    ''' 
    url - link to image, if it uploaded by url
    image - original image
    '''

    url = models.URLField(
        'Ссылка', 
        blank=True, 
        null=True)

    image = models.ImageField(
        upload_to='images/',
        blank=True, 
        null=True)

    def save(self, *args, **kwargs):
        self.get_remote_image()
        super().save(*args, **kwargs)

    def get_remote_image(self):
        '''
        For upload image from external url
        '''
        if self.url and not self.image:
            response = urlretrieve(self.url)
            self.image.save(os.path.basename(self.url), 
                                File(open(response[0], 'rb')))
            self.save()

    @property
    def get_name(self):
        '''
        For recieve the image name
        '''
        return os.path.basename(self.image.url)
