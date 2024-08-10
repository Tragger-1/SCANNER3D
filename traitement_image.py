import cv2
import numpy as np

def traitement_images(number_img,laser,paslaser):
    # reading the images 
    #laser = cv2.imread('/home/pi/images_Scanner/bl2l.png') 
    #paslaser = cv2.imread('/home/pi/images_Scanner/bl2.png') 

    if laser is None:
        print("L'image 'laser' n'a pas pu être chargée.")
    if paslaser is None:
        print("L'image 'paslaser' n'a pas pu être chargée.")
        
    height, width,_ = laser.shape
    #print("width: ", width)
    #print("height: ", height)

    img = np.zeros((height,width, 3), np.uint8)


    for i in range(height):
        for j in range(width):

            if (laser[i,j][2] >= 125): #rouge
                for k in range(0,1):
                    if(laser[i,j][k] >= paslaser[i,j][k]+25):
                        img[i,j] = paslaser[i,j] 

    #store image
    name='/home/pi/images_Scanner/RESULT_'+ str(number_img)+'.png'
    cv2.imwrite(name,img)

   
