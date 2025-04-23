import json
import numpy as np
from skimage.transform import rescale

# Load data from json file
with open('graves.json') as f:
    dat = json.load(f)

# Extract raw outline data in list format
raw = []
for i in range(len(dat)):
    coordinates = np.array(dat[i]['scaled_coordinates'])

    raw.append(coordinates)

# Reformat data to equal number of coordinates
RAW = np.array([])
for item in raw:
    r = 249.0
    resized_x = rescale(item[:, 0], r / len(item[:, 0]))
    resized_y = rescale(item[:, 1], r / len(item[:, 1]))

    resized = np.column_stack((resized_x, resized_y))

    resized = np.append(resized, np.array([resized[0]]), axis=0)
    if len(RAW) == 0:
        RAW = np.array([resized])
    else:
      RAW = np.concatenate((RAW, np.array([resized])))

# Reformat for LDA function in PAST
RAWpast = []
for i in range(len(RAW)):
    A = RAW[i][:, 0]
    B = RAW[i][:, 1]
    C = np.row_stack((A, B))
    RAWpast.append(C)

RAWpast = np.array(RAWpast).reshape(218, 250).transpose()
np.savetxt('past.csv', RAWpast, delimiter=",", fmt="%d")
