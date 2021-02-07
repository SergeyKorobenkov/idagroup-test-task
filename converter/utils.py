import mimetypes
import os

from pathlib import Path
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image

def resize(obj, height=None, width=None):
    '''
    There is we can resize our image, save it to special directory and return
    it to our main function
    '''
    BASE_DIR = Path(__file__).resolve().parent.parent

    img = Image.open(obj.image).copy()
    thumb_io = BytesIO()

    if height is None:
        height = img.height

    elif width is None:
        width = img.width

    size = (width, height)
    img.thumbnail(size, Image.ANTIALIAS)
    
    path_to_save = f'{BASE_DIR}/media/resized/' + obj.image.name[7:]
    img.save(path_to_save, format='PNG', quality=100)

    new_name = '../media/resized/' + obj.image.name[7:]
    
    return new_name

def url_validation(url, mimetype_list=['image',]):
    '''
    Check that external url contains an image
    '''
    mimetype, _ = mimetypes.guess_type(url)
    if mimetype:
        return any([mimetype.startswith(x) for x in mimetype_list])
    else:
        return False
