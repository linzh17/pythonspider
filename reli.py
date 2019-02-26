import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文乱码
pylab.mpl.rcParams['axes.unicode_minus'] = False  # 防止中文乱码


def draw_heatmap(data, xlabels, ylabels):
    cmap = cm.Blues
    figure = plt.figure(facecolor='w')
    ax = figure.add_subplot(2, 1, 1, position=[0.1, 0.15, 0.8, 0.8])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax = data[0][0]
    vmin = data[0][0]
    for i in data:
        for j in i:
            if j > vmax:
                vmax = j
            if j < vmin:
                vmin = j
    map = ax.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)
    cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    plt.xticks(rotation=90)  # 将字体进行旋转
    plt.yticks(rotation=360)
    plt.show()


#data = pd.read_csv('test.csv', encoding='gbk')
a = [[1, 2, 2, 2, 8, 2, 3, 4, 3, 2, 3, 3, 5, 2, 2, 8, 3, 5, 2, 2],
    [1, 2, 8, 8, 9, 9, 4, 4, 4, 2, 3, 1, 8, 8, 9, 9, 3, 5, 2, 2],
    [1, 2, 8, 9, 10, 9, 4, 4, 4, 2, 3, 1, 8, 10, 9, 8, 3, 5, 2, 2],
    [1, 2, 8, 9, 9, 9, 4, 4, 4, 2, 3, 1, 8, 9, 9, 9, 3, 5, 2, 2],
    [1, 2, 8, 8, 8, 8, 6, 4, 4, 2, 4, 1, 4, 7, 4, 5, 3, 5, 2, 2],
    [1, 2, 2, 2, 4, 1, 4, 6, 4, 2, 3, 1, 4, 4, 9, 9, 9, 5, 2, 2],
    [1, 2, 2, 2, 5, 1, 4, 4, 6, 6, 5, 1, 4, 4, 9, 10, 9, 5, 2, 2],
    [1, 2, 2, 2, 4, 1, 4, 4, 4, 2, 4, 6, 4, 4, 9, 9, 9, 5, 2, 2],
    [1, 2, 2, 2, 3, 1, 4, 4, 4, 2, 3, 1, 4, 4, 4, 5, 3, 5, 2, 2],
    [1, 2, 2, 2, 4, 1, 4, 4, 4, 2, 3, 1, 4, 4, 4, 4, 3, 5, 2, 2]

     ]

xlabels = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'10', u'11', u'12', u'13',
           u'14', u'15']
ylabels = ['1', '2', '3', '4', '5', '6','3', '4', '5', '6']
draw_heatmap(a, xlabels, ylabels)