import cv2
import sys
import numpy as np
from metrique import mesure
from os import listdir
from os.path import isfile, join
from def_metriques_basic import *
from def_metriques_set import *
from filler import *
from def_comptage import *
sys.path.insert(0, 'pythonEnv\\thibault')
from bibliotheque_segmentation import *

def mesure_score(image,sol,method, gray_function, seuil_threshold, iter_open, dilatation, d_transf) :
    ### Watershed_hsv
    wh_hsv = fermeture(method(image, gray_function, seuil_threshold, iter_open, dilatation, d_transf))
    wh_hsv_filled = coloriage(wh_hsv)
    imsol_f = sol
    nb_cells_sol = compt_cells_carte_contours(sol)
    euc = dist_euc(imsol_f,wh_hsv_filled)
    man = dist_manhattan(imsol_f,wh_hsv_filled)
    ncc = dist_ncc(imsol_f,wh_hsv_filled)
    jac = dist_Jaccard(imsol_f,wh_hsv_filled)
    dice = dist_Dice(imsol_f,wh_hsv_filled)
    nb_cell_wh_hsv = compt_cells_carte_contours(wh_hsv)
    #seg.append(compt_cells_mask(Liste_image[i][1]))
    score = 1  
    if (euc*man*ncc == 0) :
        score = -1
    else :
        score = jac*dice / (euc*man*ncc*100)
        if (nb_cell_wh_hsv != nb_cells_sol) : 
            score = score / (0.2*abs(nb_cell_wh_hsv-nb_cells_sol))
        else :
            score *= 10
    return score

#sol = cv2.cvtColor(cv2.imread("C:\\Users\\mazet\\OneDrive\\Documents\\paf_2022\\monuseg\\contour_gt_test\\TCGA-2Z-A9J9-01A-01-TS1_4.tif"), cv2.COLOR_BGR2GRAY)
#im = cv2.imread("C:\\Users\\mazet\\OneDrive\\Documents\\paf_2022\\monuseg\\patch_vahadane_test\\TCGA-2Z-A9J9-01A-01-TS1_4.tif")
#print(mesure_score(im,sol))
