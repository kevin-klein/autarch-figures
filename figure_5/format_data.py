import json
import numpy as np
from skimage.transform import rescale

with open('graves.json') as f:
    dat = json.load(f)

raw = []
for item in dat:
    coordinates = np.array(item['scaled_coordinates'])
    raw.append(coordinates)

RAW = np.array([])
for item in raw:
    r = 249.0
    resized_x = rescale(item[:, 0], r / len(item[:, 0]))
    resized_y = rescale(item[:, 1], r / len(item[:, 1]))

    resized = np.ravel([resized_x,resized_y], order="F")

    if len(RAW) == 0:
        RAW = np.array([resized])
    else:
      RAW = np.concatenate((RAW, np.array([resized])))

np.savetxt('output/past.csv', RAW, delimiter=",", fmt="%.3f")
