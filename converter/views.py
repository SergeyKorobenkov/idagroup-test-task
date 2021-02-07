from django.shortcuts import render, redirect, get_object_or_404

from .models import BaseImage
from .forms import ImageForm, ResizeForm
from .utils import resize


def index(request):
    '''
    Main page
    '''
    image_list = BaseImage.objects.all()
    return render(request, 'index.html', {'image_list': image_list})


def add_image(request):
    '''
    Page to add new image
    '''
    if request.method == 'POST':
        form = ImageForm(request.POST or None, files=request.FILES or None)

        if form.is_valid():
            image = form.save()
            return redirect(
                'image_details', 
                image_id=image.id)
        
    else:
        form = ImageForm()
    
    return render(
        request, 
        'add_image.html', 
        {'form': form,})


def image_details(request, image_id):
    '''
    Image details page. There is we can convert it to a new sizes and see result
    '''
    image = get_object_or_404(BaseImage, id=image_id)
    
    if request.method == 'POST':
        form = ResizeForm(request.POST or None)

        if form.is_valid():
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            resized_image = resize(image, height, width)
    
            return render(
                request, 
                'image_details.html', 
                {'form':form, 'is_resized_image':True, 'resized_image':resized_image,})
    
    else:
        form = ResizeForm()
    
    return render(
        request, 
        'image_details.html', 
        {'image': image, 'is_resized_image':False, 'form': form, })
