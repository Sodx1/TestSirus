from django.urls import path
from .views import image_list, upload_image, delete_image

urlpatterns = [
    path('upload/', upload_image, name='upload-image'),
    path('list/', image_list, name='image-list'),
    path('delete/<int:image_id>/', delete_image, name='delete-image'),
]
