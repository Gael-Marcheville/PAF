import cv2
import numpy as np

#colorie une composante connexe à la main
def coloriage_boule(image,shape,seuil,valeur,i,j):
    image[j][i] = 0
    voisins = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
    for pixel in voisins:
        (k,l) = pixel
        if k>=0 and k < shape[1] and l >= 0 and l < shape[0] :
            if image[l][k]>seuil:
                coloriage_boule(image,shape,seuil,valeur,k,l)

#pure magie #merci fonction magique + lou
def coloriage(image) :
    result = np.copy(image)
    analysis = cv2.connectedComponentsWithStats(result, 4, cv2.CV_32S )
    (totalLabels, label_ids, values, centroid) = analysis
    maxArea = 0
    maxAreaLabel = 0
    for i in range(1, totalLabels):
        area = values[i, cv2.CC_STAT_AREA]
        if (area > maxArea): 
            maxArea = area
            maxAreaLabel = i
    (m,n) = image.shape
    for i in range (m): 
        for j in range (n):
            if (label_ids[i,j] != maxAreaLabel) :
                result[i,j] = 0
    return result
    

def coloriage_2(image) :
    analysis = cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S )
    (totalLabels, label_ids, values, centroid) = analysis
    maxArea = 0
    maxAreaLabel = 0
    for i in range(1, totalLabels):
        area = values[i, cv2.CC_STAT_AREA]
        if (area > maxArea): 
            maxArea = area
            maxAreaLabel = i
    (m,n) = image.shape
    for i in range (m): 
        for j in range (n):
            if (label_ids[i,j] != maxAreaLabel) :
                image[i,j] = 0
                if (values[label_ids[i,j], cv2.CC_STAT_AREA] > 1000) :
                  image[i,j] = 125

def fermeture(image) :
    result = np.copy(image)
    (m,n) = image.shape
    for i in range (m): 
        for j in range (n):
            if (image[j][i] == 0) :
                voisins = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
                for pixel in voisins:
                    (k,l) = pixel
                    if k>=0 and k < m and l >= 0 and l < n :
                        result[l][k] = 0
    return result