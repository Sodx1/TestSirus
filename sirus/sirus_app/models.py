from django.db import models
import base64

class Image(models.Model):
    image = models.TextField()
    description = models.TextField()

    def save_base64_image(self, base64_data):
        # Декодируем base64-строку изображения
        image_data = base64.b64decode(base64_data)
        
        # Сохраняем изображение в поле модели
        self.image = image_data

        # Сохраняем модель
        self.save()
