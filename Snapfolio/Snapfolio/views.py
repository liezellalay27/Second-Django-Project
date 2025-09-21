from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'Snapfolio/index.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'Snapfolio/detail.html', {'photo': photo})

def photo_create(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'Snapfolio/create.html', {'form': form})