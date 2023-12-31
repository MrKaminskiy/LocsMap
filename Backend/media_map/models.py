from django.db import models
from django.contrib.gis.db import models as gis_models

class Media(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/')
    location = gis_models.PointField(null=True, blank=True)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

