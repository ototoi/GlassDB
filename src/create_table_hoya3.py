#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate spline interpolation.
"""
import scipy.interpolate
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

def get_valid_list(la, lb):
    l = []
    for (a, b) in zip(la,lb):
        if type(b) is float:
            l.append((a, b))
    return l

def code_to_int(s):
    s2 = s.replace('-','')
    s3 = "{0:0>6}".format(int(s2))
    return s3

nx = [
    1529.60,1128.64,1013.98,852.11,768.19,
    706.52,656.27,643.85,632.80,589.29,
    587.56,546.07,486.13,479.99,435.84,
    404.66,365.01
]

tx = [
    2500,2400,2200,2000,1800,
    1600,1550,1500,1400,1300,
    1200,1100,1060,1050,1000,
     950, 900, 850, 830, 800,
     780, 750, 700, 650, 600,
     550, 500, 480, 460, 440,
     420, 400, 390, 380, 370,
     360, 350, 340, 330, 320,
     310,
 ]

keys = "id INTEGER PRIMARY KEY,\ncode TEXT,\nname TEXT,\n";
for i in range(300, 910, 10):
    keys += "n{0} REAL,\n".format(i)

for i in range(300, 910, 10):
    keys += "t{0} REAL".format(i)
    if i != 900:
        keys += ",\n"

#print(keys)
conn = sqlite3.connect('./data/glass.sqlite3')
c = conn.cursor()
c.execute('select * from t_glass_spec_hoya')
fetched = c.fetchall()

sql = "create table t_glass_spec_hoya3 ({0})".format(keys)
c.execute('drop table t_glass_spec_hoya3')
c.execute(sql)

nList = []
tList = []
for row in fetched:
    code = row[1]
    name = row[2]
    #print(name)
    ny = list(row)[3:21]
    ll = get_valid_list(nx, ny)
    #print(ll)
    xx = [float(a) for (a,b) in ll]
    yy = [float(b) for (a,b) in ll]
    xxx = np.array(list(reversed(xx)),dtype='float32')
    yyy = np.array(list(reversed(yy)),dtype='float32')

    xn = np.arange(300, 910, 10)
    rp = scipy.interpolate.splrep(xxx, yyy, s=0)
    yn = scipy.interpolate.splev(xn, rp, der=0)
    nList.append(yn.tolist())

for row in fetched:
    code = row[1]
    name = row[2]
    #print(name)
    ny = list(row)[20:]
    ll = get_valid_list(tx, ny)
    #print(ll)
    xx = [float(a) for (a,b) in ll]
    yy = [float(b) for (a,b) in ll]
    xxx = np.array(list(reversed(xx)),dtype='float32')
    yyy = np.array(list(reversed(yy)),dtype='float32')

    xn = np.arange(300, 910, 10)
    rp = scipy.interpolate.splrep(xxx, yyy, s=0)
    yn = scipy.interpolate.splev(xn, rp, der=0)
    yn = np.maximum(yn,0)
    yn = np.minimum(yn,1)
    tList.append(yn.tolist())


keys = "\ncode,\nname,\n";
for i in range(300, 910, 10):
    keys += "n{0},".format(i)

for i in range(300, 910, 10):
    keys += "t{0}".format(i)
    if i != 900:
        keys += ", "

for i in range(len(fetched)):
    row = fetched[i]
    code = row[1]
    name = row[2]
    nl = nList[i]
    tl = tList[i]
    values = "";
    values = "null, ";
    values += "\"{0}\", ".format(str(code_to_int(code)))
    values += "\"{0}\", ".format(str(name))
    for j in range(len(nl)):
        values += str(nl[j]) + ", "
    for j in range(len(tl)):
        values += str(tl[j])
        if (j != len(tl)-1):
            values += ", "

    s = "insert into t_glass_spec_hoya3 VALUES({0})".format(values)
    c.execute(s)

conn.commit()
