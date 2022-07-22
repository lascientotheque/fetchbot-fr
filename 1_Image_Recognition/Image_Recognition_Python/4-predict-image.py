# Necessary import
import cv2 # cv2 is used to take image from the camera
import myfunctions # myfunctions helps for taking picture and making predictions
import matplotlib.pyplot as plt # matplotlib is used to deal with images
from PIL import Image # PIL is used to deal with images
import time # time is used for making the computer wait

# Get camera object
camera_object = cv2.VideoCapture(0)

# Initialize model
interpreter = myfunctions.initialize_model(model_path='model.tflite')

# Infinite loop
while True:
    
    # Wait for one second
    time.sleep(1)
    
    # Take image from the camera
    picture_rgb = myfunctions.take_picture(camera_object)
    
    # Predict image class
    prediction, probability = myfunctions.model_prediction(interpreter, picture_rgb)
    
    # If prediction is class 0, class is 'Forward'
    if prediction == 0:
        
        print("Je reconnais la classe 'Forward'")
        
    # If prediction is class 1, class is 'Other'
    if prediction == 1:
        
        print("Je reconnais la classe 'Other'")
    