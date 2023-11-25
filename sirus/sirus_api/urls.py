from django.urls import path
from sirus_api.views import ImageListCreateView, ImageView

urlpatterns = [
    path('images/', ImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageView.as_view(), name='image-detail'),
]