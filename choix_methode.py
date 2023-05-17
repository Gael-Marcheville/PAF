import random

def methode_from_class(classe) :
    methodes = ["Treshold 1", "Treshold 2", "Treshold Clean 1", "Treshold Clean 2", "Watershed bgr2gray", "Watershed clahe", "Watershed hsv"]
    p = (1,1,1,1,1,1,1)
    if (classe == 'A') :
        p = (4,11,3,15,7,2,7)
    if (classe == 'B') :
        p = (0,2,5,43,13,2,13)
    if (classe == 'C') :
        p = (0,2,0,4,0,0,0)
    if (classe == 'D') :
        p = (2,3,0,3,9,1,6)
    if (classe == 'E') :
        p = (2,22,2,7,9,0,3)
    if (classe == 'F') :
        p = (1,3,2,17,9,9,8)
    if (classe == 'G') :
        p = (11,34,0,2,0,0,2)
    if (classe == 'H') :
        p = (2,24,0,4,15,3,1)
    return random.choices(methodes, weights=p)[0]