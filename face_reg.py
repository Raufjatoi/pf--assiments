import cv2 as c
import numpy as np 
import face_recognition as fr 

img1 = fr.load_image_file('ImagesBasic/###')
img1 = c.cvtColor(img1. c.COLOR_BGR2RGB)
img2 = fr.load_image_file('ImagesBasics/###')
img2 = c.cvtColor(img2. c.COLOR_BGR2RGB)