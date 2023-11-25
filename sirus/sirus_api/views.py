from rest_framework import generics
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer


class ImageListCreateView(generics.ListCreateAPIView):
    """
    Создание картинки и описания
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        image_data = request.data.get('image_data', '')
        description = request.data.get('description', '')
        Image.objects.create(image_data=image_data, description=description)
        return Response(status=201)

class ImageView(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


