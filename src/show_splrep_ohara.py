#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate spline interpolation.
"""
import scipy.interpolate
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

nx = [
    2325.42,1970.09,1529.60,1128.64,1013.98,
    852.11,768.19,706.52,656.27,643.85,
    632.80,589.29,587.56,546.07,486.13,
    479.99,441.57,435.84,404.66,365.01
]

tx = [
    280,290,300,310,320,
    330,340,350,360,370,
    380,390,400,420,440,
    460,480,500,550,600,
    650,700,800,900,1000,
    1200,1400,1600,1800,2000,
    2200,2400
]

def get_valid_num(l):
    c = 0
    for x in l:
        if type(x) is float:
            c = c + 1
    return c

def get_valid_list(la, lb):
    l = []
    for (a, b) in zip(la,lb):
        if type(b) is float:
            l.append((a, b))
    return l


conn = sqlite3.connect('./data/glass.sqlite3')
c = conn.cursor()
c.execute('select * from t_glass_spec_ohara2')
fetched = c.fetchall()
for row in fetched:
    name = row[2]
    #print(name)
    ny = list(row)[4:24]
    ll = get_valid_list(nx, ny)
    print(ll)
    xxx = [float(a) for (a,b) in ll]
    yyy = [float(b) for (a,b) in ll]
    xx = np.array(list(reversed(xxx)),dtype='float32')
    yy = np.array(list(reversed(yyy)),dtype='float32')
    #print(xx)
    #print(yy)
    xn = np.arange(300, 901, 1)
    rp = scipy.interpolate.splrep(xx, yy, s=0)
    yn = scipy.interpolate.splev(xn, rp, der=0)
    plt.plot(xn, yn)
    #print("{0}:{1}:{2}".format(index,type(ys[16]),get_valid_num(ys)))
    #index = index +1;
plt.show()

#c.execute('select * from t_glass_spec_hoya2')
#fetched = c.fetchall()
for row in fetched:
    name = row[2]
    print(name)
    #print(row[20])
    ty = list(row)[24:]
    ll = get_valid_list(tx, ty)
    print(ll)
    xxx = [float(a) for (a,b) in ll]
    yyy = [float(b) for (a,b) in ll]
    xx = np.array(list(xxx),dtype='float32')
    yy = np.array(list(yyy),dtype='float32')
    #print(xx)
    #print(yy)
    xn = np.arange(300, 901, 1)
    rp = scipy.interpolate.splrep(xx, yy, s=0)
    yn = scipy.interpolate.splev(xn, rp, der=0)
    yn = np.maximum(yn,0)
    yn = np.minimum(yn,1)
    plt.plot(xn, yn)
    #print("{0}:{1}:{2}".format(index,type(ys[16]),get_valid_num(ys)))
    #index = index +1;
plt.show()

c.close()


"""
y = [
    1.47308,1.47774,1.47913,1.48139,1.48283,
    1.48411,1.48535,1.48569,1.48601,1.48743,
    1.48749,1.48914,1.49227,1.49266,1.49594,
    1.49896,1.50405
]
x = np.array(list(reversed(x)),dtype='float32')
y = np.array(list(reversed(y)),dtype='float32')
xn = np.arange(300, 910, 10)
rp = scipy.interpolate.splrep(x, y, s=0)
yn = scipy.interpolate.splev(xn, rp, der=0)
plt.plot(x, y)
plt.plot(xn, yn)
plt.show()

for (a,b) in zip(xn,yn):
    print("{0}:{1}".format(a,b))
"""
