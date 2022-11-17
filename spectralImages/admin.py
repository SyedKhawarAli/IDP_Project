from django.contrib import admin
from .models import SpectralImage, BinaryMasksImage

admin.site.register(SpectralImage)
admin.site.register(BinaryMasksImage)
