
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
'''# Create a neural net class
class Classifier(nn.Module):
        
    # Defining the Constructor
    def __init__(self, num_classes=17):
        super(Classifier, self).__init__()        
        # In the init function, we define each layer we will use in our model
        
        # Our images are RGB, so we have input channels = 3. 
        # We will apply 12 filters in the first convolutional layer
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        
        # A second convolutional layer takes 12 input channels, and generates 24 outputs
        self.conv2 = nn.Conv2d(in_channels=12, out_channels=24, kernel_size=3, stride=1, padding=1)
        
        # We in the end apply max pooling with a kernel size of 2
        self.pool = nn.MaxPool2d(kernel_size=2)
        
        # A drop layer deletes 20% of the features to help prevent overfitting
        self.drop = nn.Dropout2d(p=0.2)
        
        # Our 128x128 image tensors will be pooled twice with a kernel size of 2. 128/2/2 is 32.
        # This means that our feature tensors are now 32 x 32, and we've generated 24 of them
        
        # We need to flatten these in order to feed them to a fully-connected layer
        self.fc = nn.Linear(in_features=32 * 32 * 24, out_features=num_classes)

    def forward(self, x):
        # In the forward function, pass the data through the layers we defined in the init function
        
        # Use a ReLU activation function after layer 1 (convolution 1 and pool)
        x = F.relu(self.pool(self.conv1(x))) 
        
        # Use a ReLU activation function after layer 2
        x = F.relu(self.pool(self.conv2(x)))  
        
        # Select some features to drop to prevent overfitting (only drop during training)
        x = F.dropout(self.drop(x), training=self.training)
        
        # Flatten
        x = x.view(-1, 32 * 32 * 24)
        # Feed to fully-connected layer to predict class
        x = self.fc(x)
        # Return class probabilities via a log_softmax function 
        return torch.log_softmax(x, dim=1)
'''
def load_model():
    '''model=Classifier()
    state_dict = torch.load('checkpoint.pth')
    model.load_state_dict(state_dict)
    return model'''
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    loaded_model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy'])
    return load_model


def classify_img(file):
    print("classify image")
    model=load_model()
    class_names = ['Healthy', 'Mosaic', 'RedRot', 'Rust', 'Yellow']
    '''image = Image.open(file)
    x = TF.to_tensor(image)
    x=TF.resize(x,[128,128])
    print(x.shape)
    
    output = model(x)
    _, preds_tensor = torch.max(output, 1)
    preds = preds_tensor.cpu().numpy()[0]
    mapping= {0: 'BrandedChlorosis',
        1: 'BrownSpot',
        2: 'EyeSpot',
        3: 'GrassyShootDisease',
        4: 'Healthy',
        5: 'Mosiac',
        6: 'Pinapple',
        7: 'PokkhaBoeng',
        8: 'RedRot',
        9: 'Rust',
        10: 'ScaleInsects',
        11: 'Smut',
        12: 'WhiteFly',
        13: 'Wilt',
        14: 'WoollyAphid',
        15: 'YLD'}'''
    img = cv2.resize(img, (256,256))    
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    print("Predicted Class is {} with {} confidence".format(predicted_class,confidence))
    return predicted_class