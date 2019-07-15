# Get background of array of pictures
import cv2
import numpy as np
import os

def resizeImages(fileNames, numFiles):
    # Resize images by certain amount
    resizedImages = []
    for i in range(0,numFiles):
        img = cv2.imread(imageNames[i],0)
        resized = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
        resizedImages.append(resized)
    return resizedImages

def averageImage(imageArray, dimensions):
    # All images have to be of same dimensions in this version
    img = imageArray[0]
    numFiles = len(imageArray)
    height, width = dimensions
    avgPixels = [] #Array to store average intensity of each pixel
    step = 1

    for i in range(0,width,step):
        for j in range(0,height,step):

            sum = 0

            for k in range(0,numFiles):
                img = imageArray[k]
                sum += img[j,i]

            avgPixel = sum/numFiles

            avgPixels.append(avgPixel/255)

    averagedImage = np.reshape(avgPixels, (int(width/step), int(height/step)))
    return averagedImage

def showImageFromFile(fileName):
    # Reads image from file and displays
    if os.path.isfile(fileName):
        img = cv2.imread(fileName,0)
        cv2.imshow('image', img);
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('File not found')
    return img

def showImage(imageName):
    # Displays image from variable
    cv2.imshow('image', imageName)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getFileSize(imagePath): #Returns file size in bytes
    statinfo = os.stat(imagePath)
    size = statinfo.st_size
    return size




imageNames = []
numFiles = 14 # Number of files to be averaged

for i in range(1,numFiles+1):
    fileName = 'img' + str(i) + '.jpg' # Creating file names e.g "img1.jpg"
    imageNames.append(fileName)

resized = resizeImages(imageNames,numFiles)
avg = averageImage(resized, resized[0].shape)

showImage(avg) # Show final image without moving subject
