import numpy
from numpy import genfromtxt
from matplotlib import pyplot as plt

d = genfromtxt('../data.csv', delimiter=',')

d = d[1:,:]

fig,ax = plt.subplots()

heatmap = ax.pcolor(d)

xlabels = ['X','Y','PHI','IR1','LDR1','IR2','LDR2','IR3','LDR3','IR4','LDR4','IR5','LDR5','IR6','LDR6','IR7','LDR7','IR8','LDR8']

ax.set_xticks(numpy.arange(0,19))

ax.set_xticklabels(xlabels)

plt.show()
