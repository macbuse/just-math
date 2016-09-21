# coding: utf-8
#
import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

sample_dimension = 30000
sample_size = 300

def mk_copies(x):
    A  = np.ones([sample_size,sample_dimension])
    y = A*x
    return y.transpose()

u = np.random.random(sample_dimension)
v = np.random.random(sample_dimension)
u,v = 2*u - 1, 2*v -1

u = u / np.linalg.norm(u)
v = v - np.dot(u,v)*u
v = v / np.linalg.norm(v)

T = np.linspace(0, 2*np.pi,sample_size)

u = mk_copies(u)
v = mk_copies(v)

circle_pts  = np.cos(T)*u + np.sin(T)*v

all_ones = np.ones(sample_dimension)
one_norms =  np.dot(all_ones, np.abs(circle_pts ) )
coeff = 1./one_norms

X = np.ones_like(u)
X[0] = np.cos(T)
X[1] = np.sin(T)

X = coeff*X

plt.plot(X[0],X[1], 'xr')
plt.show()






