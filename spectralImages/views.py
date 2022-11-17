from django.shortcuts import render
from .models import SpectralImage
from .spectral_tiffs import read_stiff
# import matplotlib.pyplot as plt
# from django.http import HttpResponse
# import numpy as np
# from os import listdir
# from os.path import isfile, join
import os


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

def getFileNameFromFolder():
    path = "spectralImages/flat-fielded"
    return os.listdir(path)


def getNameOfFileWithOutExtension(file):
    return os.path.splitext(file)[0]

def saveDataIntoTable(files):
    spectralImages = SpectralImage.objects
    if not spectralImages.exists():
        for index, file in enumerate(files):
            image = SpectralImage(index, getNameOfFileWithOutExtension(file), file)
            image.save()
    else :
        print("Already added in database")

            
def home(request):
    files = getFileNameFromFolder()
    saveDataIntoTable(files)
    
    context = {
        'spectralImages': SpectralImage.objects.all(),
    }
    # onlyfiles = [f for f in listdir(
        # 'spectralImages') if isfile(join('spectralImages', f))]

    # print(cube, wavelengths, preview_image, metadata)
    # print(cube)
    f = open("demofile.txt", "w")
    # for file in files:
    #     print(getNameOfFileWithOutExtension(file))
    # print(len(cube))
    # print(len(cube[0]))
    # print(len(cube[0][0]))
    # for value in cube:
    #     print(len(value))
    #     for item in value:
    #         print(len(item))
            # f.write(str(item))
    # print(f.read())
    return render(request, 'spectralImages/home.html', context)
    # plt.plot(wavelengths, cube[511, 511, :])
    # return HttpResponse("<h1>Test</h1>")
