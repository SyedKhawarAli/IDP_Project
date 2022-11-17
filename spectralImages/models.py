from django.db import models
from django.utils import timezone

class SpectralImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)

    # def __int__(self):
    #     return self.id
