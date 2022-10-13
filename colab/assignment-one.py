import numpy as np
import math

def distance(a, b):
  return np.linalg.norm(a-b)

def perimeter(figure):
  a = np.array((figure[0], figure[1]))
  b = np.array((figure[2], figure[3]))
  c = np.array((figure[4], figure[5]))
  if len(figure) > 6:
    d = np.array((figure[6], figure[7]))
    perimeter = (distance(a, b) + distance(b, c) + distance(c, d) + distance(d, a))
  else:
    perimeter = (distance(a, b) + distance(b, c) + distance(c, a))
  return perimeter

def heron(a, b, c):
  s = (a + b + c) / 2
  return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_triangle(figure):
  a1 = np.array((figure[0], figure[1]))
  b1 = np.array((figure[2], figure[3]))
  c1 = np.array((figure[4], figure[5]))

  a = distance(a1, b1)
  b = distance(b1, c1)
  c = distance(c1, a1)
  return heron(a, b, c)

def area_square(figure):
  a1 = np.array((figure[0], figure[1]))
  b1 = np.array((figure[2], figure[3]))
  a = distance(a1, b1)
  return a**2

def area_rectangle(figure):
  a1 = np.array((figure[0], figure[1]))
  b1 = np.array((figure[2], figure[3]))
  c1 = np.array((figure[4], figure[5]))

  a = distance(a1, b1)
  b = distance(b1, c1)
  return a*b

def area_rhombus(figure):
  a = np.array((figure[0], figure[1]))
  b = np.array((figure[2], figure[3]))
  c = np.array((figure[4], figure[5]))
  d = np.array((figure[6], figure[7]))

  d1 = distance(a, c)
  d2 = distance(b, d)
  return (d1*d2)/2

def centroid_triangle(figure):
  sumx = []
  sumy = []
  for pos in range(len(figure)):
    if pos%2 == 0:
      sumx.append(figure[pos])
    else:
      sumy.append(figure[pos])
  return (round(sum(sumx)/3), round(sum(sumy)/3))

def centroid_square(figure):
  a1 = np.array((figure[0], figure[1]))
  b1 = np.array((figure[2], figure[3]))
  c1 = np.array((figure[4], figure[5]))

  a = distance(a1, b1)
  b = distance(b1, c1)
  return (round(a/2), round(b/2))

def centroid_rhombus(figure):
  a = np.array((figure[0], figure[1]))
  b = np.array((figure[2], figure[3]))
  c = np.array((figure[4], figure[5]))
  d = np.array((figure[6], figure[7]))

  d1 = distance(a, c)
  d2 = distance(b, d)
  return (round(d2/2), round(d1/2))

with open(file_path, 'r') as f:
    lines = f.readlines()

names = []
shapes = []
coordinates = []

for line in lines:
    line = line.strip()
    line = line.split(' ')
    image_name = line[0]
    names.append(image_name)

    shapes.append((image_name.strip()).split('_')[1][:-4])
    coord = line[1:]
    coordinates.append([int(x) for x in coord])

# List of perimeters
result_perimeter = []
for num in coordinates:
  result_perimeter.append(round(perimeter(num)))

# List of areas
result_area = []
for pos in range(len(shapes)):
  if shapes[pos] == 'triangle':
    result_area.append(round(area_triangle(coordinates[pos])))
  elif shapes[pos] == 'square':
    result_area.append(round(area_square(coordinates[pos])))
  elif shapes[pos] == 'rectangle':
    result_area.append(round(area_rectangle(coordinates[pos])))
  else:
    result_area.append(round(area_rhombus(coordinates[pos])))

# List of centroids
result_centroid = []
for pos in range(len(shapes)):
  if shapes[pos] == 'triangle':
    result_centroid.append(centroid_triangle(coordinates[pos]))
  elif shapes[pos] == 'square' or shapes[pos] == 'rectangle':
    result_centroid.append(centroid_square(coordinates[pos]))
  else:
    result_centroid.append(centroid_rhombus(coordinates[pos]))

for x in range(len(names)):
  print('Name:', names[x], '- Perimeter:', result_perimeter[x],
        '- Area:', result_area[x], '- Centroid:', result_centroid[x])

