#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate spline interpolation.
"""
import scipy.interpolate
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import math

def get_valid_list(la, lb):
    l = []
    for (a, b) in zip(la,lb):
        if type(b) is float:
            l.append((a, b))
    return l

def code_to_int(s):
    #s2 = str(float(s)).replace('-','')
    s3 = "{0:0>6}".format(int(s))
    return s3

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
c.execute('select * from t_glass_spec_schott')
fetched = c.fetchall()

sql = "create table t_glass_spec_schott3 ({0})".format(keys)
c.execute('drop table t_glass_spec_schott3')
c.execute(sql)

nList = []
tList = []
for row in fetched:
    code = row[1]
    name = row[0]
    #print(name)
    ny = list(row)[32:]
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
    name = row[0]
    #print(name)
    ty = list(row)[2:32]
    ll = get_valid_list(tx, ty)
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
    name = row[0]
    code = row[1]
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

    s = "insert into t_glass_spec_schott3 VALUES({0})".format(values)
    c.execute(s)

conn.commit()
