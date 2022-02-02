import numpy as np
import scipy.misc as mi
im = mi.imread('obj1__0.png')
from scipy.misc.pilutil import Image
im= Image.open('obj1__0.png')
import matplotlib.pyplot as plt
plt.imshow(np.uint8(im))
plt.show()
