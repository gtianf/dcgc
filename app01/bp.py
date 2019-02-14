# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dcgc.settings")
import django
django.setup()
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://gtianf:123456.@localhost:3306/dcgc')
sql = 'select standard_p,standard_t,u,uu,t,ut,tt from app01_raw_data where rom_id="6800 DC20 1608 1729"'
data = pd.read_sql_query(sql, engine)
#选择需要回归的自变量
feature_cols = ['u', 'uu', 't', 'ut', 'tt']
# X = np.array(data[feature_cols])
# print(X)
X = np.array([[6025,36300625,1401,8441025,1962801],
 [6540,42771600,1401,9162540,1962801],
 [7054,49758916,1401,9882654,1962801],
 [6934,48080356,1134,7863156,1285956]])
# y = np.array(data['standard_p']])
y = np.array([[250],[300],[350],[300]])
print(y)
# n = len(list(y))
# print(n)

def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    if -x > np.log(np.finfo(type(x)).max):
        return 0.0
    a = np.exp(-x)
    return 1.0/(1.0+a)


# X = np.array([[0, 0, 1],
#               [0, 1, 1],
#               [1, 0, 1],
#               [1, 1, 1]])

# y = np.array([[0],
#               [1],
#               [1],
#               [0]])

np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2 * np.random.random((5, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for j in range(60000):

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # how much did we miss the target value?
    l2_error = y - l2

    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error * nonlin(l2, deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)


print(l2)
