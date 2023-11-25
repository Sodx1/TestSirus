from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sirus_api.urls')), 
    path('interface/', include('image_interface.urls'))
]