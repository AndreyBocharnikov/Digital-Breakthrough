from google.colab import drive
import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize
import itertools
from sklearn.preprocessing import StandardScaler
import torch
from torch import nn
import glob
import os
import cv2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from torch.utils import data
from PIL import Image
import torchvision
import time

def read_json(file_path):
  file_name = open(file_path, "r")
  content = file_name.read()
  file_name.close()
  return json.loads(content)
def write_json(file_path, content):
  file_name = open(file_path, "w")
  json.dump(content, file_name)
  file_name.close()

def make_descriptions_and_images():
  size = 261
  n_classes = 6
  descriptions, images = [], []
  for i in range(1, size + 1):
    index = str(i)
    while (len(index) < 3):
      index = '0' + index
    descriptions.append(read_json('/content/drive/My Drive/ml_contests/digital_breakthrough/train/' + index + '.json'))
    im = cv2.imread('/content/drive/My Drive/ml_contests/digital_breakthrough/train/' + index + '.png')
    images.append(im)
  return (descriptions, images)

def make_labels_and_classes(descriptions):
  labels = {}
  index_to_class = []
  for index, desc in enumerate(descriptions):
    current_label = desc['shapes'][0]['label']
    current_label_val = labels.get(current_label, None)
    index_to_class.append(current_label)
    if current_label_val is None:
      labels[current_label] = [index]
    else:
      labels[current_label].append(index)

  classes = list(labels.keys())
  class_to_index = {classes[index]:index for index in range(6)}

  return (labels, classes, class_to_index)
