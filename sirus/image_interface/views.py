from django.shortcuts import render, redirect
from .forms import ImageForm
import requests


API_BASE_URL = "http://localhost:8000/api/images/"

def image_list(request):
    response = requests.get(API_BASE_URL)
    images = response.json()
    return render(request, 'image_list.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_data = request.FILES['image_data'].read()
            description = form.cleaned_data['description']
            data = {'description': description, 'image_data': image_data}
            response = requests.post(API_BASE_URL, data=data)
            if response.status_code == 201:
                return redirect('image-list')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def delete_image(request, image_id):
    delete_url = f"{API_BASE_URL}{image_id}/"
    response = requests.delete(delete_url)
    if response.status_code == 204:
        return redirect('image-list')
    else:
        pass