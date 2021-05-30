import tensorflow as tf
from tensorflow import keras
import numpy as np
import PIL
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
new_model = tf.keras.models.load_model('app/saved_model/my_model')
def recognizaion(name):
    img = keras.preprocessing.image.load_img('app/saved_image/'+name, target_size=(180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return np.argmax(score), 100 * np.max(score)