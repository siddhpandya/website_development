from django.shortcuts import render, redirect
from .forms import MediaUploadForm
from .models import MediaUpload

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = MediaUploadForm()
    return render(request, 'upload_media.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

def media_list(request):
    media = MediaUpload.objects.all()
    return render(request, 'media_list.html', {'media': media})