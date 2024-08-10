# importing OpenCV library 
from cv2 import *
def Photos(): 
    # initialize the camera 
    # If you have multiple camera connected with  
    # current device, assign a value in cam_port  
    # variable according to that 
    cam_port = 0
    cam = VideoCapture(cam_port) 
    
    # reading the input using the camera 
    result, image = cam.read() 
    
    # If image will detected without any error,  
    # show result 
    #if result: 
        # saving image in local storage 
        #imwrite("/home/pi/images_Scanner/capture.jpg.png", image) 
    # If captured image is corrupted, moving to else part 
    #else: 
        #print("No image detected. Please! try again") 

    print("Photos prises")
    return image