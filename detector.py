# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:50:50 2020

@author: Praneet Shetty
"""


#detector.py
from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np
import os

model = load_model('model_saved.h5') #Load our model

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

test_image=[] #List which will store all the image to be passed for prediction

path=r"C:/Users/Praneet Shetty/Desktop/Image/test"
for img in os.listdir(path):
    imge = image.load_img(r"C:/Users/Praneet Shetty/Desktop/Image/test/"+img, target_size=(48,48,3))
    imge = image.img_to_array(imge)
    imge = imge/255
    test_image.append(imge)

test = np.array(test_image)
l=len(test)
d=model.predict_classes(test)

for i in range(l):
    if (d[i] == 0):
        print("1")
    else:
        print("0")

## for single image prediction
img = cv2.imread('G0011953.jpg')#input the image name
img = cv2.resize(img,(48,48))
img = np.reshape(img,[1,48,48,3])

d=model.predict_classes(img)

if (d == 1):
    print("0")
else:
    print("1")    
