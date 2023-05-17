import cv2
import numpy as np

def convert_gray(im) :
    if (len(im.shape) == 3) :
        return cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    return im

#méthode simple, problème : si décalage, très mauvaise valeure de corrélation

def dist_euc(im1, im2) :
    im1_gray = convert_gray(im1)
    im2_gray = convert_gray(im2)
    dist = np.where(im1_gray > im2_gray, ((im1_gray - im2_gray)/255)**2, ((im2_gray - im1_gray)/255)**2)
    S = np.sqrt(np.sum(dist/np.size(dist)))
    return S

def dist_manhattan(im1, im2) :
    im1_gray = convert_gray(im1)
    im2_gray = convert_gray(im2)
    dist = np.where(im1_gray > im2_gray, ((im1_gray - im2_gray)/255), ((im2_gray - im1_gray)/255))
    S = np.sum(dist)/np.size(dist)
    return S

def moy_gray(im1) :
    return np.sum(im1)/np.size(im1)

def dist_ncc(im1, im2) :
    im1_gray = convert_gray(im1)
    im2_gray = convert_gray(im2)
    moy1 = moy_gray(im1_gray)
    moy2 = moy_gray(im2_gray)
    dist = np.abs(((im1_gray - moy1) * (im2_gray - moy2)))
    S = np.sum(dist)/ (np.size(im1_gray) *np.std(im1_gray) *np.std(im2_gray) * 255)
    return S

def im_align(im1,im2) :
    im1_gray = convert_gray(im1)
    im2_gray = convert_gray(im2)
    orb_detector = cv2.ORB_create(5000) # Create ORB detector with 5000 features.
    kp1, d1 = orb_detector.detectAndCompute(im1_gray, None) # Find keypoints and descriptors.
    kp2, d2 = orb_detector.detectAndCompute(im2_gray, None) # The first arg is the image, second arg is the mask
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) # Match features between the two images.  We create a Brute Force matcher with Hamming distance as measurement mode.
    matches = matcher.match(d1, d2) # Match the two sets of descriptors.
    matches = sorted(matches, key=lambda x: x.distance)
    #matches.sort(key = lambda x: x.distance) # Sort matches on the basis of their Hamming distance.
    matches = matches[:int(len(matches)*0.9)] # Take the top 90 % matches forward.
    no_of_matches = len(matches)
    p1 = np.zeros((no_of_matches, 2)) # Define empty matrices of shape no_of_matches * 2.
    p2 = np.zeros((no_of_matches, 2))
    for i in range(len(matches)):
        p1[i, :] = kp1[matches[i].queryIdx].pt
        p2[i, :] = kp2[matches[i].trainIdx].pt
    homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC) # Find the homography matrix.
    height, width = im2_gray.shape
    transformed_img = cv2.warpPerspective(im1, homography, (width, height)) # Use this matrix to transform the colored image wrt the reference image.
    return transformed_img


