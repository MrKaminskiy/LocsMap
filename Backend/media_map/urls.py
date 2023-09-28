from django.urls import path
from .views import upload_image, get_images  # Убедитесь, что здесь нет MediaViewSet

urlpatterns = [
    path('media/upload/', upload_image, name='upload_image'),
    path('media/get_images/', get_images, name='get_images'),
]
