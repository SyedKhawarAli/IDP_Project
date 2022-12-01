from django.db import models
from django.utils import timezone


class SpectralImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class BinaryMasksImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    spectral_image = models.ForeignKey(SpectralImage, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
