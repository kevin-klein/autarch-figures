import matplotlib.markers
from pyefd import elliptic_fourier_descriptors, reconstruct_contour
import json
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA
import numpy as np
import awkward as ak

with open('graves.json', 'r') as f:
  data = json.load(f)

cw = []
bb = []

for item in data:
  if item['culture_label'] == 'CW':
    cw.append(item)
  else:
    bb.append(item)

cw_data = []
for item in cw:
  coeffs = elliptic_fourier_descriptors(item['scaled_coordinates'], order=20, normalize=True)
  cw_data.append(np.array(coeffs).flatten())

bb_data = []
for item in bb:
  coeffs = elliptic_fourier_descriptors(item['scaled_coordinates'], order=20, normalize=True)
  bb_data.append(np.array(coeffs).flatten())

cw_data = np.asarray(cw_data)
bb_data = np.asarray(bb_data)

pca = PCA(n_components=2)
pca.fit(np.append(cw_data, bb_data, axis=0))

cw_pca = pca.transform(cw_data)
bb_pca = pca.transform(bb_data)

rc = {"xtick.direction" : "inout", "ytick.direction" : "inout",
      "xtick.major.size" : 5, "ytick.major.size" : 5,}
with plt.rc_context(rc):
    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(12, 12))

    ax1.spines['left'].set_position('zero')
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')

    xticks = np.arange(-0.25, 0.25, 0.05)
    xlabels = [f'{x:1.2f}' for x in xticks]
    ax1.set_xticks(xticks, labels=xlabels)
    ax1.set_axisbelow(True)

    ax1.set_xlim(-0.5, 0.5)

    ax1.axis('equal')

    ax1.scatter(cw_pca[:, 0], cw_pca[:, 1], marker='s', c='#2B83BA', label='Corded Ware')
    ax1.scatter(bb_pca[:, 0], bb_pca[:, 1], marker='^', c='#d7191c', label='Bell Beaker')
    ax1.legend()

    ax1.set_xlabel(f'EFA PC1 {(pca.explained_variance_ratio_[0] * 100):.1f}%', loc='left')
    ax1.set_ylabel(f'EFA PC2 {(pca.explained_variance_ratio_[1] * 100):.1f}%', loc='bottom', rotation=0, labelpad=15)

    all_data = np.append(cw_data, bb_data, axis=0)
    all_pca_data = np.append(cw_pca, bb_pca, axis=0)
    max_x = np.max(all_pca_data[:, 0])
    max_y = np.max(all_pca_data[:, 1])

    min_x = np.min(all_pca_data[:, 0])
    min_y = np.min(all_pca_data[:, 1])

    for x_step in np.arange(min_x, max_x, 0.05):
      for y_step in np.arange(min_y, max_y, 0.05):
        x_indices = np.where(np.logical_and(all_pca_data[:, 0] >= x_step, all_pca_data[:, 0] <= x_step + 0.05))
        y_indices = np.where(np.logical_and(all_pca_data[:, 1] >= y_step, all_pca_data[:, 1] <= y_step + 0.05))

        indices = np.intersect1d(x_indices, y_indices)

        values = all_data[indices]

        contours = np.array([reconstruct_contour(contour.reshape((20, 4))) for contour in values])

        if len(contours) == 0:
          continue

        average_contour = np.average(contours, axis=0)
        ax2.spines['left'].set_position('zero')
        ax2.spines['right'].set_visible(False)
        ax2.spines['bottom'].set_position('zero')
        ax2.spines['top'].set_visible(False)
        ax2.xaxis.set_ticks_position('bottom')
        ax2.yaxis.set_ticks_position('left')

        ax2.axis('equal')
        ax2.xaxis.set_ticks([])
        ax2.yaxis.set_ticks([])

        ax2.set_xlim(-0.6, 2)

        ax2.fill(average_contour[:, 0] + (x_step * 45) + 1.5, average_contour[:, 1] + (y_step * 40) + 1.5, '#A9A9A9')

    cw_coordinates = ak.Array([item['scaled_coordinates'] for item in cw])
    bb_coordinates = ak.Array([item['scaled_coordinates'] for item in bb])

    cw_coordinates = (cw_coordinates - ak.mean(cw_coordinates)) / ak.std(cw_coordinates)
    bb_coordinates = (bb_coordinates - ak.mean(bb_coordinates)) / ak.std(bb_coordinates)

    ax3.axis('equal')

    for item in cw_coordinates:
      ax3.plot(item[:, 0] - 5, item[:, 1], linewidth=0.4, color='#AAA')

    # average_cw_efd = np.average(non_normalized_cw_data.reshape(len(non_normalized_cw_data), 20, 4), axis=0)
    # average_cw_contour = reconstruct_contour(average_cw_efd)
    # ax3.plot((average_cw_contour[:, 0] * ak.ptp(cw_coordinates[:, 0]) / 2) - 5, (average_cw_contour[:, 1] * ak.ptp(cw_coordinates[:, 1]) / 2), linewidth=0.5, color='#2B83BA')

    for item in bb_coordinates:
      ax3.plot(item[:, 0] + 5, item[:, 1], linewidth=0.4, color='#AAA')

    # average_bb_efd = np.average(non_normalized_bb_data.reshape(len(non_normalized_bb_data), 20, 4), axis=0)
    # average_bb_contour = reconstruct_contour(average_bb_efd)
    # ax3.plot((average_bb_contour[:, 0] * ak.ptp(bb_coordinates[:, 0]) / 2) + 5, (average_bb_contour[:, 1] * ak.ptp(bb_coordinates[:, 1]) / 2), linewidth=1, color='#d7191c')

    ax3.set_axis_off()

    plt.savefig("output/figure_5.png", dpi=600)
