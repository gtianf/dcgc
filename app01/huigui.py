# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dcgc.settings")
import django
django.setup()
import numpy as np
from sklearn import linear_model,metrics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from sklearn.cross_decomposition import tra
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://gtianf:123456.@localhost:3306/dcgc')
sql = 'select standard_p,standard_t,u,uu,t,ut,tt from app01_raw_data where rom_id="B901 DC22 1801 1728"'
data = pd.read_sql_query(sql, engine)
#选择需要回归的自变量
feature_cols = ['u', 'uu', 't', 'ut', 'tt']
X = data[feature_cols]
#需要回归的因变量
Y = data['standard_p']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0, random_state=1)
linreg = LinearRegression()
model = linreg.fit(X_train, Y_train)
#获取截距
intercept = linreg.intercept_
#把x值带入系数求解y值
test_set = linreg.predict(X)
# #获取残差列表
ck_list = Y - test_set
#获取系数
#p, pp, t, pt, tt = linreg.coef_
#score = linreg.score(X,Y)
# print(ck_list)
#平均值
# mean = np.mean(ck_list)
# #中位数
# median = np.median(ck_list)
#极差
# ptp = np.ptp(ck_list,axis=None,out=None)
#方差
# var = np.var(ck_list)
# #标准差
# std = np.std(ck_list)
# #协方差
#cov = np.cov(ck_list)
print(ck_list)
# #最大值
# max = np.max(ck_list)
# #最小值
# min = np.min(ck_list)
# #获取拟合度
# score = linreg.score(X,Y)
# print("平均值=%.16f,中位数=%.16f,方差=%.16f,标准差=%.16f,协方差=%.16f,拟合率=%.16f,最大值=%.16f,最小值=%.16f"%(mean,median,var,std,cov,score,max,min))
# print(np.where(ck_list==np.max(ck_list)))
# #
# print(ck_list)
# print(max(ck_list))
# print(min(ck_list))
# print(np.mean(ck_list))

percent = (np.sum(ck_list>0.5) + np.sum(ck_list<-0.5))/len(list(ck_list))
if percent <= 0.1:
    level = 1
elif percent > 0.1 and percent <= 0.2:
    level = 2
elif percent > 0.2 and percent <= 0.3:
    level = 3
elif percent > 0.3:
    level = 0
print(level)

