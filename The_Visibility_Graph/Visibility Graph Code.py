# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:12:24 2022

@author: satvik
"""

import matplotlib.pyplot as plt
from visibility_graph import visibility_graph


def conway_series_gen(var_):

    series_ = {1:1,2:1}

    if var_ == 1:
        series_ = {1:1}
    elif var_ == 2:
        series_ = {1:1,2:2}
    else:
        for n_ in range(3,var_+1):
            #series_[n_] = series_[(series_[series_[(n_-1)]])] + series_[(n_-(series_[(n_-1)]))]
            series_[n_] = series_[series_[(n_-1)]] + series_[n_ - (series_[(n_-1)])]

    return series_

def ySide(var):
    yValues = []
    for key,value in var.items():
        temp = series_[key] - key/2
        yValues.append(temp)
    return yValues

series_ = conway_series_gen(10)

xpoints = []
ypoints = ySide(series_)
for a in series_:
    xpoints.append(a)

plt.bar(xpoints,ypoints)
plt.xlabel("n")
plt.ylabel("a(n) - n/2")

g = visibility_graph(xpoints)
nodes = g.nodes()
print("nodes: " + str(nodes))
edges = g.edges()
print("edges: " + str(edges))