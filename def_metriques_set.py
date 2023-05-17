import cv2
import numpy as np

def convert_gray(im) :
    if (len(im.shape) == 3) :
        return cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    return im

def dist_Jaccard(im1, im2) :
    im1_gray = convert_gray(im1)
    im2_gray = convert_gray(im2)
    return np.sum(np.logical_and(im1_gray, im2_gray)) / np.sum(np.logical_or(im1_gray,im2_gray))

def dist_Dice(im1, im2) :
    im1_gray = convert_gray(im1)
    im2_gray = convert_gray(im2)
    return 2*256*np.sum(np.logical_and(im1_gray, im2_gray)) / (np.sum(im1_gray) + np.sum(im2_gray))