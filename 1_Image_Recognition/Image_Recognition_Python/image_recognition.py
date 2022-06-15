# Necessary import
import cv2 # cv2 is used to take image from the camera
import myfunctions # myfunctions helps for taking picture and making predictions
import matplotlib.pyplot as plt # matplotlib is used to deal with images
from PIL import Image # PIL is used to deal with images
import time # time is used for making the computer wait

# Get camera object
camera_object = cv2.VideoCapture(0)

# Take a picture from the camera
picture_rgb = myfunctions.take_picture(camera_object)

# Display picture
picture_as_image_object = Image.fromarray(picture_rgb)
plt.imshow(picture_as_image_object)