from django.db import models
from django.utils import timezone


class BinaryMasksImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class SpectralImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    mask_image = models.ForeignKey(BinaryMasksImage, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    