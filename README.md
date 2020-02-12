# Image-Classification
All the code and data used for training and testing purpose are compressed and uploaded in the github in the name of Image.zip

1: The python file image.py is the python File which on executing will train our CNN model and will save the model for further use.While executing make sure you give the Ccorrect path of the training and validation datas. This python file trains the CNN model taking the Training data with 25 epochs.The CNN model has 3 Convolution layer and 2 Fully connected layer .

2:The python File Detector.py is executed once the image.py is executed and the trained CNN model[model_saved.h5] is saved for further use.This file will load and compile the saved CNN model[model_saved.h5].The model will take all the N testing images and will classify the images as 0 [Good image] and 1[Flare Image]. Make sure the path of the test data is correctly given.
This file can also be used for testing of single image ,which can be don by just passing the Image name .[Make sure the path and the image path location are same]

3: Before excuting make sure you macine has already installed Keras and CV2.
