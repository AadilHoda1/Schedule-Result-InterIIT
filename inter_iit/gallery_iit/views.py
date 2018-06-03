from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from gallery_iit.models import Image
from gallery_iit.models import Video
# from gallery_iit.models import Item
from gallery_iit.forms import ImageForm
from gallery_iit.forms import VideoForm

from PIL import Image as Img
# import PIL.Image

# def index(request):
#     return render(request, 'index.html')

def home(request):

    images = Image.objects.all()
    videos = Video.objects.all()
    # embeded = Item.objects.all()



    for temp in images:
    #     fp = open(temp.image, "rb")
    #     img = PIL.Image.open(fp)
        im = Img.open(temp.image.path)
        im.save(temp.image.path, quality=50, optimize=True)
        im.close()

    return render(request, 'gallery_iit.html', {'images': images, 'videos': videos,})


def model_form_upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {
        'form': form
    })


def model_form_upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload.html', {
        'form': form
    })





