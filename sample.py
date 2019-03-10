import cv2
import numpy as np
import dominantcolor
from PIL import Image
import greendetect
import cropmin
img2 = cv2.imread("593.png")
img1=greendetect.maskgreen(img2)
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
row, col= img.shape[:2]
bottom= img[row-2:row, 0:col]
mean= cv2.mean(bottom)[0]

bordersize=10
img=cv2.copyMakeBorder(img, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[mean,mean,mean])

#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#mask = cv2.inRange(hsv, lower_red, upper_red)
#img = cv2.bitwise_and(img, img, mask=mask)
#kernel = np.ones((15, 15), np.float64)/225
#blur = cv2.GaussianBlur(img, (5,5), 0)
#ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_ BINARY+cv2.THRESH_OTSU)
bilateral=cv2.bilateralFilter(img,15,15,15)
#eats a lot of processing power
edgesbilateral=cv2.Canny(bilateral,170,170)
#edgesblur=cv2.Canny(blur,50,50)
#edges=cv2.Canny(img,50,50)
ret, thresh = cv2.threshold(bilateral, 130, 255, 0)
contours,h=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contoursx=cv2.drawContours(img,contours, -1, (255,255,255), 3)
a=[]
b=[]  
for i in contours:
    b.append(cv2.contourArea(i))  
for i in contours:        
    if cv2.contourArea(i)<100 and cv2.contourArea(i)>=50:
        a.append(i) 
a=np.asarray(a)
#print(a) 
#gaus=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,1)
kernel=np.ones((2,2),np.uint8) 
#opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
#closing=cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel)   
contours1=cv2.drawContours(img,a, -1, (255,255,255), 3)
for i in a:   
    x,y,w,h = cv2.boundingRect(i)          
    cv2.rectangle(contours1,(x,y),(x+w,y+h),(255,255,255),2)
    #rect = cv2.minAreaRect(i)
    #c=cropmin.crop_minAreaRect(img1,rect)
    #cv2.imshow("idk",c)
    j=img1[y-10:y+h+10,x-10:x+w+10]
    k=img[y-10:y+h+10,x-10:x+w+10]
    t=dominantcolor.dominant(j)
    #print(t)
    temp=False   #returns dominant hsv value of image
    temp=greendetect.greendetect(t)    #detects if green or not 
    if temp!=True:
        #greendetect.maskgreen(j) 
        #ta=dominantcolor.dominant(o)
        #print(ta)
        y=greendetect.col_detect(t)
        if y!=None:
            print(y)
            print(t)
            cv2.imshow("cropped",j) 
        else:
            print('This image is not classified for color')
            cv2.imshow('cropped',j)
        cv2.waitKey(0)
    #cv2.imshow('k',j)
    #cv2.waitKey(0)
'''imrgb=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
i=Image.fromarray(imrgb)'''
#dominantcolor.dominant(img1) 
#blur=cv2.GaussianBlur(thresh, (3,3), 0)  
cv2.imshow('img', img)  
#dominantcolor.dominant(i) 
cv2.imshow('bi',bilateral)  
#cv2.imshow('blur',blur)
#cv2.imshow('otsu',th3)
#cv2.imshow('gaus',edgesblur)
cv2.imshow('bilateral',edgesbilateral) 
#cv2.imshow('imge', edges) 
#cv2.imshow('gaus',gaus)
cv2.imshow('contthresh',contours1)
#cv2.imshow('thresh',thresh)
cv2.waitKey(0) 
cv2.destroyAllWindows()

