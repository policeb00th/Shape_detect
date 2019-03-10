from PIL import Image
import cv2
import numpy as np

def dominant(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    #img.show()
    w, h = img.size
    pixels = img.getcolors(w * h)
    #print(pixels)
    pixels.sort()
    most_frequent_pixel = pixels[-2] 
    '''for count, colour in pixels:
        if count >most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)'''
    #compare("Most Common", img, most_frequent_pixel[1])
    #print("True")
    (R,G,B)=most_frequent_pixel[1]
    k=np.uint8([[[B,G,R]]])
    l=cv2.cvtColor(k,cv2.COLOR_BGR2HSV)
    t=l[0][0]
    print((B,G,R),"-BGR VALS")
    return t
