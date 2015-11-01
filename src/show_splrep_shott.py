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
    2325.4,# REAL,--n2325.4
    1970.1,# REAL,--n1970.1
    1529.6,# REAL,--n1529.6
    1060.0,# REAL,--n1060.0
    1014.0,# REAL,--nt
    852.1,# REAL,--ns
    706.5,# REAL,--nr
    656.3,# REAL,--nC
    643.8,# REAL,--nC'
    632.8,# REAL,--n632.8
    589.3,# REAL,
    587.6,# REAL,
    546.1,# REAL,
    486.1,# REAL,
    480.0,# REAL,--nF'
    435.8,# REAL,
    404.7,# REAL,
    365.0,# REAL,
    334.1,# REAL,--n334.1
    312.6,# REAL,--n312.6
    296.7,# REAL,--n296.7
    280.4,# REAL,--n280.4
    248.3 # REAL--n248.3
]

tx = [
    2500,2325,1970,1530,1060,
    700,660,620,580,546,
    500,460,436,420,405,
    400,390,380,370,365,
    350,334,320,310,300,
    290,280,270,260,250
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
c.execute('select * from t_glass_spec_schott')
fetched = c.fetchall()
for row in fetched:
    name = row[0]
    #print(name)
    ny = list(row)[32:]
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

print(len(fetched))
#c.execute('select * from t_glass_spec_hoya2')
#fetched = c.fetchall()
for row in fetched:#range(fetched:
    name = row[0]
    print(name)
    #print(row[23])
    ty = list(row)[2:32]
    ll = get_valid_list(tx, ty)
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
