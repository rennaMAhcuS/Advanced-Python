# from random import random
#
# x = int(100 * random())
# print(x)
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
y = np.array([1, 3, 5, 7])

plt.plot(x, y, marker="o", ms=20, mec="r", mfc="b", ls="-.")
plt.show()
