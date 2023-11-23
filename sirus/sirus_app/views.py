from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sirus_app.models import Image
from sirus_app.serializers import ImageSerializer

class ImageList(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class ImageDelete(APIView):
    def delete(self, request, image_id):
        try:
            image = Image.objects.get(pk=image_id)
            image.delete()
            return Response(status=204)
        except Image.DoesNotExist:
            return Response(status=404)