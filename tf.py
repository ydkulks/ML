#Simple Linear Regression
import tensorflow as tf
import matplotlib as mp
mp.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d

x = [1, 2, 2.5, 3, 4]
y = [1, 4, 7, 9, 15]
plt.plot(x, y, 'o')
plt.axis([0,20,0,20])
plt.plot(np.unique(x),np.poly1d(np.polyfit(x,y,1))(np.unique(x)))
print("Line of best fit: ",np.unique(x),np.poly1d(np.polyfit(x,y,1))(np.unique(x)))
plt.show() 
