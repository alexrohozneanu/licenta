import numpy as np
import imutils
import cv2
import math
import copy

def rotAndTrans(img):

    i=0
    j=0

    while(img[i][50]<=20):
        i+=1

    while(img[j][750]<=20):
        j+=1

    rotated=imutils.rotate(img,math.atan((j-i)/700)*180/math.pi)
    k=0
    while(rotated[k][400]<=20):
        k+=1
    l=0
    while(rotated[150][l]<=20):
        l+=1
    i=0
    m=np.shape(rotated)[0]-1
    while(rotated[m][400]<=20):
        m-=1
        i+=1
    j=0
    n=799
    while(rotated[150][n]<=20):
        n-=1
        j+=1
    rotandtrans=imutils.translate(rotated,(j-l)/2,(i-k)/2)


    k=0
    rot=copy.copy(rotandtrans)
    while(rotandtrans[k][400]<=20):
        k+=1
    if(k>5):
        rot=rot[k-5:np.shape(rot)[0],0:np.shape(rot)[1]]
    l=0
    while(rotandtrans[150][l]<=20):
        l+=1
    if(l>5):
        rot=rot[0:np.shape(rot)[0],l-5:np.shape(rot)[1]]
    i=0
    m=np.shape(rot)[0]-1
    while(rot[m][400]<=20):
        m-=1
        i+=1
    if(i>5):
        rot=rot[0:m+5,0:np.shape(rot)[1]]
    j=0
    n=np.shape(rot)[1]-1

    while(rot[150][n]<=20):
        n-=1
        j+=1
    if(j>5):
        rot=rot[0:np.shape(rot)[0],0:n+5]
    print(k)
    print(l)
    print(i)
    print(j)
    print(np.shape(rot))
    rot=cv2.resize(rot,(800,280))
    return rot
