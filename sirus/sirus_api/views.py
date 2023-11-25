import base64
import io

from rest_framework import generics
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer


class ImageListCreateView(generics.ListCreateAPIView):
    """
    GET, POST функции работы 
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        image_data_str = request.data.get('image_data', '')
        description = request.data.get('description', '')

        image_data = base64.b64decode(image_data_str)

        Image.objects.create(image_data=image_data, description=description)
        return Response(status=201)

class ImageView(generics.RetrieveDestroyAPIView):
    """
    DELETE Функции работы
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


