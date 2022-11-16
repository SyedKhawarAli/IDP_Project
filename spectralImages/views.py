from django.shortcuts import render
from .models import SpectralImage
from .spectral_tiffs import read_stiff
import matplotlib.pyplot as plt
from django.http import HttpResponse
import numpy as np
from os import listdir
from os.path import isfile, join


spectralImages = [
    {
        'title': 'Spectral image 1',
        'path': 'spectralImages/AI_Gurus.png',
        'date_posted': '28 August, 2022'
    },
    {
        'title': 'Spectral Image 2',
        'path': 'IDP_Project/spectralImages/AI_Gurus.png',
        'date_posted': '28 August, 2022'
    }
]

cube, wavelengths, preview_image, metadata = read_stiff(
    "spectralImages/Set 1, lower 2, icg.tif")


def home(request):
    context = {
        'spectralImages': spectralImages #SpectralImage.objects.all()
    }
    # onlyfiles = [f for f in listdir(
        # 'spectralImages') if isfile(join('spectralImages', f))]

    # print(onlyfiles)
    return render(request, 'spectralImages/home.html', context)
    # plt.plot(wavelengths, cube[511, 511, :])
    # return HttpResponse("<h1>Test</h1>")
