# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
from keras import backend as K
import numpy as np
import os

model_file_name = 'digits_model.h5'
classes_file_name = 'classes.txt'

def train():

    script_dir = os.path.abspath(os.path.dirname(__file__))
    dir = os.path.join(script_dir, "../../" + model_file_name)

    # Initialising the CNN
    exists = os.path.isfile(dir)

    if exists:
        print('Loading model from file')
        classifier = load_model(dir)
    else:

        classifier = Sequential()

        # Step 1 - Convolution
        classifier.add(Conv2D(32, (3, 3), input_shape = (128, 128, 3), activation = 'relu'))

        # Step 2 - Pooling
        classifier.add(MaxPooling2D(pool_size = (2, 2)))

        # Adding a second convolutional layer
        classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
        classifier.add(MaxPooling2D(pool_size = (2, 2)))

        # Step 3 - Flattening
        classifier.add(Flatten())

        # Step 4 - Full connection
        classifier.add(Dense(units = 128, activation = 'relu'))
        classifier.add(Dense(units = 10, activation = 'sigmoid'))

        # Compiling the CNN
        classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

        # Part 2 - Fitting the CNN to the images

        from keras.preprocessing.image import ImageDataGenerator

        train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

        test_datagen = ImageDataGenerator(rescale = 1./255)

        training_set = train_datagen.flow_from_directory('digits_dataset/training_set',
                                                 target_size = (128, 128),
                                                 batch_size = 32)

        test_set = test_datagen.flow_from_directory('digits_dataset/test_set',
                                            target_size = (128, 128),
                                            batch_size = 32)

        classifier.fit_generator(training_set,
                         steps_per_epoch = 1000,
                         epochs = 3,
                         validation_data = test_set,
                         validation_steps = 300)

        print('Saving model!')
        classifier.save(dir)
        print('Save success!')

# Part 3 - Making new predictions

#
#from keras.preprocessing import image
#test_image = image.load_img('digits_dataset/single_prediction/dig.png', target_size = (64, 64))
#test_image = image.img_to_array(test_image)
#test_image = np.expand_dims(test_image, axis = 0)
#result = classifier.predict(test_image)

#if result[0][0] == 1:
#    prediction = 'dog'
#else:
#    prediction = 'cat'

#print(result)

def recognize(imagePath):
    script_dir = os.path.abspath(os.path.dirname(__file__))
    dir = os.path.join(script_dir, "../../" + model_file_name)
    print(dir)
    classifier = load_model(dir)
    imagePath = os.path.join(script_dir, "../" + imagePath)
    print(imagePath)
    #imagePath = "/webpath/webpart/" + imagePath
    test_image = image.load_img(imagePath, target_size=(128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    print(result)
    classes = get_classes()
    recognized = []
    i = 0
    while i < len(classes):
        if result[0][i] != 0:
            recognized.append(classes[i])
        i = i + 1

    K.clear_session()
    return recognized

def get_classes():
    script_dir = os.path.abspath(os.path.dirname(__file__))
    dir = os.path.join(script_dir, "../../" + classes_file_name)
    with open(dir) as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        lines[i] = lines[i].strip()
        i = i + 1

    return lines


#train()