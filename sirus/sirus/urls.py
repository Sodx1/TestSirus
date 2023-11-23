
from django.urls import path
from sirus_app.views import ImageList, ImageDelete

urlpatterns = [
    path('images/', ImageList.as_view()),
    path('images/<int:image_id>/', ImageDelete.as_view()),
]