from django.db import models
from django.utils import timezone

class SpectralImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
