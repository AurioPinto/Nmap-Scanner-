import cv2
import matplotlib.pyplot as plt
import numpy as np


flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

len(flags)

flags[40]

nemo = cv2.imread('/home/ap_tech/Pictures/West.jpg')
plt.imshow(nemo)
plt.show()
