# Scatter Plot Matrix

import matplotlib.pyplot as plt
import pandas

from pandas.tools.plotting import scatter_matrix

url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

pandas.DataFrame.hist(data)

scatter_matrix(data)
plt.show()

