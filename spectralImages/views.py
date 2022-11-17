from django.shortcuts import render
from .models import SpectralImage, BinaryMasksImage
from .spectral_tiffs import read_stiff
import os

#read sample image for testing
cube, wavelengths, preview_image, metadata = read_stiff(
    "spectralImages/Set 1, lower 2, icg.tif")

def getFlatFieldedImagesNameFromFolder():
    path = "spectralImages/flat-fielded"
    return os.listdir(path)


def getBinaryMasksImagesNameFromFolder():
    path = "spectralImages/binary-masks"
    return os.listdir(path)

def getNameOfFileWithOutExtension(file):
    return os.path.splitext(file)[0]

def saveFlatFieldedDataIntoTable(files):
    spectralImages = SpectralImage.objects
    if not spectralImages.exists():
        for index, file in enumerate(files):
            SpectralImage(index, getNameOfFileWithOutExtension(file), file).save()            
    else :
        print("Already added in database")
        
def saveBinaryMaskDataIntoTable(files):
    binaryMasksImages = BinaryMasksImage.objects
    if not binaryMasksImages.exists():
        for index, file in enumerate(files):
            BinaryMasksImage(index, getNameOfFileWithOutExtension(file), file).save()
    else :
        print("Already added in database")     

def home(request):
    flatFieldFiles = getFlatFieldedImagesNameFromFolder()
    saveFlatFieldedDataIntoTable(flatFieldFiles)
    binaryMasksFiles = getBinaryMasksImagesNameFromFolder()
    saveBinaryMaskDataIntoTable(binaryMasksFiles)

    context = {
        'spectralImages': SpectralImage.objects.all(),
    }
    # print(cube, wavelengths, preview_image, metadata)
    # f = open("demofile.txt", "w")
    # print(len(cube))
    # print(len(cube[0]))
    # print(len(cube[0][0]))
    # for value in cube:
    #     print(len(value))
    #     for item in value:
    #         print(len(item))
            # f.write(str(item))
    return render(request, 'spectralImages/home.html', context)