import os
import cv2
import numpy as np
from metrique import mesure
from os import listdir
from os.path import isfile, join

def etude_classe(letter):
    noms_tiff = [f for f in listdir('pythonEnv\\Data\\classes\\classe' + letter) if isfile(join('pythonEnv\\Data\\classes\\classe' + letter, f))]
    methodes = ["Treshold 1", "Treshold 2", "Treshold Clean 1", "Treshold Clean 2", "Watershed bgr2gray", "Watershed clahe", "Watershed hsv"]
    methodes_iteration = [0,0,0,0,0,0,0]

    for tiff in noms_tiff :
        sol = cv2.cvtColor(cv2.imread('pythonEnv\\Data\\contour_gt_test\\' + tiff), cv2.COLOR_BGR2GRAY)
        im = cv2.imread('pythonEnv\\Data\\classes\\classe' + letter + '\\' + tiff)
        mes = mesure(im,sol)
        scores = []
        methodes_tiff = []
    # print('--------')
        for seg in mes[1] :
            score = 1  
            if (seg[1]*seg[2]*seg[3] == 0) :
                score = -1
            else :
                score = seg[4]*seg[5] / (seg[1]*seg[2]*100*seg[3])
                if (seg[6] != mes[0]) : 
                    score = score /  np.sqrt(abs(mes[0]-seg[6]))
                else :
                    score *= 2
            scores.append(score)
        index_score_max = np.argmax(scores)
        methodes_iteration[index_score_max] += 1



        #print('--------')
        #print(methodes[index_score_max] + " est la meilleure méthode pour " + tiff + " avec un score de " + str(scores[index_score_max]))
    print("Classe " + letter)
    for i in range (len(methodes)) :
        print(methodes[i] + " a été choisie " + str(methodes_iteration[i]) + " fois")

for x in ['A','B','C','D','E','F','G','H'] :
    etude_classe(x)