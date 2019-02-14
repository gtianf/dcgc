# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dcgc.settings")
import django
django.setup()
from app01 import db


# sql = "select * from ProjectTree limit 10"
# ms = db.MySql()
# res_list = ms.ExecQuery(sql)
# for row in res_list:
# 	print(row)

###最小二乘法试验###
import numpy as np
from scipy.optimize import leastsq

###采样点(Xi,Yi)###
Ui=np.array([1401,1401,1401,1401,1401])
U2i=np.array([1962801,1962801,1962801,1962801,1962801])
Ti=np.array([5509,6025,6540,7054,7565])
TUi=np.array([7718109,8441025,9162540,9882654,10598565])
T2i=np.array([30349081,36300625,42771600,49758916,57229225])
Yi=np.array([200,250,300,350,400])
###需要拟合的函数func及误差error###
def func(p,u,u2,t,tu,t2):
    a0,a1,a2,a3,a4,a5 = p
    return a0+a1*u+a2*u2+a3*t+a4*tu+a5*t2
def error(p,u,u2,t,tu,t2,y,s):
    print(s)
    return func(p,u,u2,t,tu,t2)-y #x、y都是列表，故返回值也是个列表
#TEST
p0=[5,2,10,100,200,300]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的a~c
Para=leastsq(error,p0,args=(Ui,U2i,Ti,TUi,T2i,Yi,s)) #把error函数中除了p以外的参数打包到args中
#a0,a1,a2,a3,a4,a5=Para[0]
#print("a0=%d,a1=%d,a2=%d,a3=%d,a4=%d,a5=%d" %(a0,a1,a2,a3,a4,a5))

###绘图，看拟合效果###
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(8,6))
# plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
# x=np.linspace(-5,5,1000)
# y=a0+a1*u+a2*u2+a3*t+a4*tu+a5*t2
# plt.plot(x,y,color="orange",label="Fitting Curve",linewidth=2) #画拟合曲线
# plt.legend()
# plt.show()