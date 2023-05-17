import cv2

def compt_cells_carte_contours(image) :
    analysis = cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S )
    (totalLabels, label_ids, values, centroid) = analysis
    #
    maxArea = 0
    maxAreaLabel = 0
    for i in range(1, totalLabels):
        area = values[i, cv2.CC_STAT_AREA]
        if (area > maxArea): 
            maxArea = area
            maxAreaLabel = i
    #
    average = 0
    for i in range (1, totalLabels):
        if (i != maxAreaLabel):
            average = average + values[i, cv2.CC_STAT_AREA]
    average = average/totalLabels
    seuil = 0.5*average
    cpt = 0
    for i in range(1, totalLabels):
        area = values[i, cv2.CC_STAT_AREA] 
        if (area > seuil):
            cpt += 1
    return cpt - 1

def compt_cells_mask(image) :
    image = cv2.bitwise_not(image)
    analysis = cv2.connectedComponentsWithStats(image, 4, cv2.CV_32S )
    return analysis[0]
