
import matplotlib.pyplot as plt
'''
from torch import nn, optim
import torch.nn.functional as F
from PIL import Image
import torchvision.transforms.functional as TF
import torch
from torchvision import datasets, transforms,models
import numpy as np'''
import numpy as np
from tensorflow.keras.models import Sequential, model_from_json
import cv2
import tensorflow as tf
def load_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    '''loaded_model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy'])'''
    return loaded_model


def classify_img(file):
    print("classify image")
    model=load_model()
    class_names = ['Healthy', 'Mosaic', 'RedRot', 'Rust', 'Yellow']
    img = cv2.imread(file)
    img = cv2.resize(img, (256,256))  
    img=img/255  
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    print("Predicted Class is {} with {} confidence".format(predicted_class,confidence))
    return predicted_class,img