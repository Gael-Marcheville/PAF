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

def mesure(image,sol) :
    Liste_image = []
    Liste_nom = []
    ### Treshold methode
    Liste_image.append((None, segmentation1_elouan(image)))
    Liste_nom.append("Treshold 1")
    Liste_image.append((None,segmentation2_elouan(image)))
    Liste_nom.append("Treshold 2")
    Liste_image.append((None,clean(Liste_image[0][1])))
    Liste_nom.append("Treshold Clean 1")
    Liste_image.append((None,clean(Liste_image[1][1])))
    Liste_nom.append("Treshold Clean 2")

    thresh_min = threshold_minimum(image, bgr2gray_settings)
    ### Watershed_method_clahe
    wh1 = fermeture(watershed_method(image, bgr2gray_without_settings, thresh_min, 2, 5, 0.5))
    Liste_image.append((wh1,coloriage(wh1))) #C'est très très bon, mais il manque 1 noyau et quelques imprécisions
    Liste_nom.append("Watershed bgr2gray")
    wh1 = fermeture(watershed_method(image, clahe, thresh_min, 2, 5, 0.5))
    Liste_image.append((wh1,coloriage(wh1))) #C'est très très bon, mais il manque 1 noyau et quelques imprécisions
    Liste_nom.append("Watershed clahe")
    ### Watershed_hsv
    wh_hsv = fermeture(watershed_method(image, hsv, thresh_min, 2, 5, 0.4))
    Liste_image.append((wh_hsv,coloriage(wh_hsv))) #ok mais sans plus
    Liste_nom.append("Watershed hsv")

    imsol_f = sol

    nb_cells = compt_cells_carte_contours(sol)
    result = []

    for i in range (len(Liste_image)) :
        seg = []
        seg.append(Liste_nom[i])
        seg.append(dist_euc(imsol_f,Liste_image[i][1]))
        seg.append(dist_manhattan(imsol_f,Liste_image[i][1]))
        seg.append(dist_ncc(imsol_f,Liste_image[i][1]))
        seg.append(dist_Jaccard(imsol_f,Liste_image[i][1]))
        seg.append(dist_Dice(imsol_f,Liste_image[i][1]))
        """
        print("---------------------")
        print(Liste_nom[i])
        print("Distance euclidienne : " + str(dist_euc(imsol_f,Liste_image[i][1])))
        print("Distance manhattan : " + str(dist_manhattan(imsol_f,Liste_image[i][1])))
        print("Distance corrélation croisée normalisée : " + str(dist_ncc(imsol_f,Liste_image[i][1])))
        print("Indice de Jaccard : " + str(dist_Jaccard(imsol_f,Liste_image[i][1])))
        print("Indice de Dice : " + str(dist_Dice(imsol_f,Liste_image[i][1])))
        """
        if (i > 3) :
            seg.append(compt_cells_carte_contours(Liste_image[i][0]))
            #print("Nombre de noyaux detectés : " + str(compt_cells_carte_contours(Liste_image[i][0])) + " sur " + nb_cells)
        else :
            seg.append(compt_cells_mask(Liste_image[i][1]))
            #print("Nombre de noyaux detectés : " + str(compt_cells_mask(Liste_image[i][1])) + " sur " + nb_cells)
        result.append(seg)
    return nb_cells,result