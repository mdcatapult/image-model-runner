# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:41:31 2020

@author: anastasia.ioannidou
"""
import argparse
import os
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import yaml


def classify_images(img_source, config_file):
    """
    Returns a zipped List with:
        a) the paths of all images in the specified folder, and
        b) the classes predicted from the provided model.
    """
    ## IMAGES
    # Save all images that need to be processed to a list.
    img_list = []

    if os.path.isdir(img_source):
        # Loop through image directory and get all images paths.
        for r, d, f in os.walk(img_source):
            for file in f:
                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.bmp') or file.endswith('.tiff'):
                    img_list.append(os.path.join(r, file))
    else:
        img_list.append(img_source)

    ## CONFIG
    with open(config_file, "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    # MODEL/CLASSIFICATION
    predictions = []
    if cfg["model"]["framework"] == 'keras':
        model = load_model(cfg["model"]["filename"])

        # Process images and get the predictions from the model.
        for i in range(0, len(img_list)):
            img = image.load_img(img_list[i], target_size=(model.input_shape[1], model.input_shape[2]))

            imgArr = image.img_to_array(img)

            if cfg["model"]["preprocessing"]["scale"] == True:
                imgArr = imgArr / 255.0

            imgArr = np.expand_dims(imgArr, axis=0)

            prediction = model.predict(imgArr)
            pred = prediction.argmax(axis=1)[0]

            if cfg["model"]["labels"]:
                predictions.append(cfg["model"]["labels"][pred])
            else:
                predictions.append(pred)
    return list(zip(img_list, predictions))

# Parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--config", type=str,
    help="Path to config YAML file.")
ap.add_argument("-d", "--imageDir", type=str,
    help="Path to directory with images to test.")
args = vars(ap.parse_args())

# Classify.
# predictions = classify_images("mdc_comp_test_data", "config.yml")
predictions = classify_images(args["imageDir"], args["config"])

# Display the results.
for image_file, pred in predictions:
    print("{},{}".format(image_file, pred))
