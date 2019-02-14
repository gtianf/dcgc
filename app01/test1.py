# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dcgc.settings")
import django
django.setup()
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  # 能快速读取常规大小的文件。Pandas能提供高性能、易用的数据结构和数据分析工具
from sklearn.utils import shuffle  # 随机打乱工具，将原有序列打乱，返回一个全新的顺序错乱的值
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://gtianf:123456.@localhost:3306/dcgc')
sql = 'select standard_t,u,uu,t,ut,tt,standard_p from app01_raw_data where rom_id="B901 DC22 1801 1728"'
# 读取数据文件
#df = pd.read_csv("data/boston.csv", header=0)

data = pd.read_sql_query(sql, engine)
X = np.array([[6025,36300625,1401,8441025,1962801],
 [6540,42771600,1401,9162540,1962801],
 [7054,49758916,1401,9882654,1962801],
 [6934,48080356,1134,7863156,1285956]])
# y = np.array(data['standard_p']])
y = np.array([[250],[300],[350],[300]])
# print(df)
x_train = np.array([[6025,36300625,1401,8441025,1962801],
 [6540,42771600,1401,9162540,1962801],
 [7054,49758916,1401,9882654,1962801],
 [6934,48080356,1134,7863156,1285956]])
y_train = np.array([[250],[300],[350],[300]])
import tensorflow as tf

X = tf.placeholder(tf.float32, [None, 5])
w = tf.Variable(tf.zeros([5, 1]))
b = tf.Variable(tf.zeros([1]))
y = tf.matmul(X, w) + b
Y = tf.placeholder(tf.float32, [None, 1])

# 成本函数 sum(sqr(y_-y))/n
cost = tf.reduce_mean(tf.square(Y-y))

# 用梯度下降训练
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)



for i in range(10000):
    sess.run(train_step, feed_dict={X: x_train, Y: y_train})
print("w0:%f" % sess.run(w[0]))
print("w1:%f" % sess.run(w[1]))
print("b:%f" % sess.run(b))
