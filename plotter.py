import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from matplotlib.colors import ListedColormap, BoundaryNorm

data = scipy.io.loadmat('base_data/Indian_pines_corrected.mat')['indian_pines_corrected']
labels = scipy.io.loadmat('base_data/Indian_pines_gt.mat')['indian_pines_gt']

classes = """
Background
Alfalfa
Corn-notill
Corn-mintill
Corn
Grass-pasture
Grass-trees
Grass-pasture-mowed
Hay-windrowed
Oats
Soybean-notill
Soybean-mintill
Soybean-clean
Wheat
Woods
Buildings-Grass-Trees-Drives
Stone-Steel-Towers
"""

cs = classes.split("\n")
css = []
for c in cs:
    if len(c.strip()) != 0:
        css.append(c)

unique_labels = np.unique(labels)
print(unique_labels)
encoded_labels = LabelEncoder().fit_transform(labels.ravel()).reshape(labels.shape)

colors = ['black'] + list(plt.cm.tab20.colors[:len(unique_labels)-1])
cmap = ListedColormap(colors)
norm = BoundaryNorm(boundaries=np.arange(len(unique_labels)+1)-0.5, ncolors=len(unique_labels))

plt.figure(figsize=(10, 10))
img = plt.imshow(encoded_labels, cmap=cmap, norm=norm)

cbar = plt.colorbar(img, shrink=0.65)
cbar.set_label('Classes', fontsize=20)
cbar.set_ticks(unique_labels)
cbar.set_ticklabels(css)
cbar.ax.tick_params(length=0, which='both')
plt.subplots_adjust(right=0.8)
label = cbar.ax.yaxis.label
#label.set_position((0.6, 1.07))
plt.xticks([])
plt.yticks([])
#plt.show()
plt.savefig("cmap_ip.png")
