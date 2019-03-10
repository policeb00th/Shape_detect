import cv2
import numpy as np
#yell=np.uint8([[[0,0,0]]])
#hsvyell=cv2.cvtColor(yell,cv2.COLOR_BGR2HSV)
#print(hsvyell)

def greendetect(t):
    if t[0] in range(38,85):
        if t[1] in range(25,256):
            if t[2] in range(25,256):
                return True
def maskgreen(j):
    lg=np.array([29,25,25])
    ug=np.array([90,256,256])
    hsv=cv2.cvtColor(j,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lg,ug)
    mask_inv=cv2.bitwise_not(mask)
    res=cv2.bitwise_and(j,j,mask=mask_inv)
    return res

def unmaskgreen(j):
    lg=np.array([29,25,25])
    ug=np.array([90,256,256])
    hsv=cv2.cvtColor(j,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lg,ug)
    mask_inv=cv2.bitwise_not(mask)
    res=mask
    return res
def col_detect(t):
    if t[0] in range(0,5) or t[0] in range(175,181):
        if t[1] in range(50,256):
            if t[2] in range(50,256):
                return('Red')
    if t[0] in range (8,19):
        if t[1] in range(50,256):
            if t[2] in range(50,256):
                return('Orange')
    elif t[0] in range(25,38):
        if t[1] in range(50,256):
            if t[2] in range(50,256):
                return('Yellow')
    elif t[0] in range(110,130):
        if t[1] in range(50,256):
            if t[2] in range(50,256):
                return('Blue')
    elif t[0] in range(140,160):
        if t[1] in range(50,256):
            if t[2] in range(50,256):
                return('Purple')
    elif t[0] in range (0,180):
        if t[1] in range(0,5):
            if t[2] in range(245,256):
                return('White')