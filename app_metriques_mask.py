import sys
sys.path.insert(0, 'pythonEnv\\Elouan')
sys.path.insert(0, 'pythonEnv\\Lou')
sys.path.insert(0, 'pythonEnv\\thibault')
from def_metriques_basic import *
from filler import *
from segmentation import *
from def_comptage import *
from def_metriques_set  import *
from clean_cells import *
from bibliotheque_segmentation import *

Liste_image = []
Liste_nom = []

img_result = cv2.imread('pythonEnv\\Data\\contour\\TCGA-2Z-A9J9-01A-01-TS1_0.tif') 
cv2.imshow('img', img_result)
img_result_gray_carte = cv2.cvtColor(cv2.imread('pythonEnv\\Data\\contour\\TCGA-2Z-A9J9-01A-01-TS1_0.tif'), cv2.COLOR_BGR2GRAY)
img_result_gray = coloriage(img_result_gray_carte)
cv2.imshow('result', img_result_gray)
cv2.waitKey(0)

### Treshold methode
Liste_image.append((None, segmentation1(cv2.imread('pythonEnv\\Data\\patch_vahadane\\TCGA-2Z-A9J9-01A-01-TS1_0.tif'))))
Liste_nom.append("Treshold 1")
Liste_image.append((None,segmentation2(cv2.imread('pythonEnv\\Data\\patch_vahadane\\TCGA-2Z-A9J9-01A-01-TS1_0.tif'))))
Liste_nom.append("Treshold 2")
Liste_image.append((None,clean(Liste_image[0][1])))
Liste_nom.append("Treshold Clean 1")
Liste_image.append((None,clean(Liste_image[1][1])))
Liste_nom.append("Treshold Clean 2")

### Watershed_method_clahe
wh1 = fermeture(watershed_method(image, clahe, threshold_minimum(image, bgr2gray_settings), 2, 5, 0.4))
Liste_image.append((wh1,coloriage(wh1))) #C'est très très bon, mais il manque 1 noyau et quelques imprécisions
Liste_nom.append("Watershed clahe 1")
wh1 = fermeture(watershed_method(image, clahe, threshold_minimum(image, bgr2gray_settings), 2, 5, 0.5))
Liste_image.append((wh1,coloriage(wh1))) #C'est très très bon, mais il manque 1 noyau et quelques imprécisions
Liste_nom.append("Watershed clahe 2")
### Watershed_hsv
wh_hsv = fermeture(watershed_method(image, hsv, 10, 2, 5, 0.4))
Liste_image.append((wh_hsv,coloriage(wh_hsv))) #ok mais sans plus
Liste_nom.append("Watershed hsv")

imsol_f = img_result_gray

nb_cells = str(compt_cells_carte_contours(img_result_gray_carte))

for i in range (len(Liste_image)) :
    print("---------------------")
    print(Liste_nom[i])
    print("Distance euclidienne : " + str(dist_euc(imsol_f,Liste_image[i][1])))
    print("Distance manhattan : " + str(dist_manhattan(imsol_f,Liste_image[i][1])))
    print("Distance corrélation croisée normalisée : " + str(dist_ncc(imsol_f,Liste_image[i][1])))
    print("Indice de Jaccard : " + str(dist_Jaccard(imsol_f,Liste_image[i][1])))
    print("Indice de Dice : " + str(dist_Dice(imsol_f,Liste_image[i][1])))
    if (i > 3) :
       print("Nombre de noyaux detectés : " + str(compt_cells_carte_contours(Liste_image[i][0])) + " sur " + nb_cells)
    else :
        print("Nombre de noyaux detectés : " + str(compt_cells_mask(Liste_image[i][1])) + " sur " + nb_cells)

#print("distance euclidienne après alignement :")
#print(dist_euc(im_align(im1,im2),im2))

#cv2.imshow('Solution', imsol_f)
#cv2.imshow('Result seg clean 1', im1_f)
#cv2.imshow('Result seg clean 2', im2_f)
#cv2.waitKey(0)