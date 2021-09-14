from django.shortcuts import render, redirect

from library.models import PhotoModel
from library.forms import PhotoForm


def photo_list(request):
    photos = PhotoModel.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'pages/photo_list.html', {'form': form, 'photos': photos})