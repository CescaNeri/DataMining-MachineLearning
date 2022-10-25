import numpy as np
import math
from sklearn.metrics import accuracy_score
from numpy.lib.twodim_base import histogram2d
import cv2
from google.colab.patches import cv2_imshow


#Load Data

#!unzip -q Euclid_dataset.zip -d /content/dataset
dataset_path = '/content/dataset/Euclid_dataset'

from os.path import join
s1 = 'path1'
s2 = 'path2'
s3 = 'path3'
print('Final path:', join(s1, s2, s3))

from glob import glob
elements = glob(join(dataset_path, '*'))
print(len(elements), elements)

shapes = ['triangle', 'rectangle', 'square', 'rhombus']
for shape in shapes:
    images = glob(join(dataset_path, shape, '*.png'))

images = glob(join(dataset_path, '*', '*.png'))

# Functions

def compute_accuracy(gt, pred):
  counter = 0
  for n in range(len(pred)):
    if pred[n] == gt[n]:
      counter += 1
  return counter / len(pred)

def first_not_zero(histo):
  for i, v in enumerate(histo):
    if v > 0:
      return i
  return None

def start_end_histo(histo):
  start = first_not_zero(histo)
  end = first_not_zero(histo[::-1])
  return start, end

def position(img):
  xs, xe, ys, ye = [], [], [], []
  for i in range(img.shape[0]):
    column = img[i, :]
    s, e = start_end_histo(column)
    if s != None:
      xs.append(s)
      xe.append(e)
  for j in range(img.shape[1]):
    row = img[:, j]
    s, e = start_end_histo(row)
    if s != None:
      ys.append(s)
      ye.append(e)
  return xs, xe, ys, ye

def clean(histogram):
  return [x for x in histogram if x != 0]

def all_roughly_equal(histogram):
  return np.var(histogram) < 0.5

def square(xs, xe, ys, ye):
  return rectangle(xs, xe, ys, ye) and len(xs) == len(ys)

def rectangle(xs, xe, ys, ye):
  return all_roughly_equal(xs) and all_roughly_equal(xe) and all_roughly_equal(ys) and all_roughly_equal(ys)

def difference(side):
  return [side[value + 1] - side[value] for value in range(len(side) - 1)]

def valid_rhombus_profile(profile):
  mid = len(profile)//2
  first_half = profile[0:mid]
  second_half = profile[mid::]
  diff_x = difference(first_half)
  diff_y = difference(second_half[::-1])
  tot_diff = diff_x + diff_y
  if all_roughly_equal(tot_diff):
    return np.average(tot_diff)
  else:
    return None

def absolute_difference(s, e):
  return abs(s - e) < 1

def rhombus(xs, xe, ys, ye):
  validxs, validxe = valid_rhombus_profile(xs), valid_rhombus_profile(xe)
  validys, validye = valid_rhombus_profile(ys), valid_rhombus_profile(ye)  
  if validxs != None and validxe != None:
    if validys != None and validye != None:
      return absolute_difference(validxs, validxe) and absolute_difference(validys, validye)
  else:
    return None 

def classify(img):
  w, h = img.shape
  black_image = img.copy()
  cv2.floodFill(black_image, None, (0, 0), 0)
  cv2.floodFill(black_image, None, (w-1, 0), 0)
  cv2.floodFill(black_image, None, (0, h-1), 0)
  cv2.floodFill(black_image, None, (w-1, h-1), 0)
  xs, xe, ys, ye = position(black_image)
  if len(xs) == 0 or len(xe) == 0 or len(ys) == 0 or len(ye) == 0:
    return 0
  if square(xs, xe, ys, ye):
    return 2
  elif rectangle(xs, xe, ys, ye):
    return 1
  elif rhombus(xs, xe, ys, ye):
    return 3
  else:
    return 0

ground_truth = []
prediction = []

for path in images:
  img = cv2.imread(path, 0)
  #cv2_imshow(img)
  label = get_labels(path)
  ground_truth.append(label)
  p = classify(img)
  prediction.append(p)
  
  # if label == 0 and p == 2:
  #   cv2_imshow(img)
  #   print('----------------')
  #print(compute_histo_by_lines(img))

print(prediction)
print(ground_truth)

print([(a, b) for a,b in zip(ground_truth, prediction) if a != b])

print(compute_accuracy(ground_truth, prediction))