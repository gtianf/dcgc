from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import xlrd
import datetime
from xlrd import xldate_as_tuple
import os
import time
from django.core.paginator import Paginator
import numpy as np
from sklearn import linear_model,metrics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sqlalchemy import create_engine
# Create your views here.
count = 0
def insert_db(file_name):
	book = xlrd.open_workbook(file_name)
	sheet1 = book.sheet_by_index(0)
	nrows = sheet1.nrows
	ncol = sheet1.ncols
	titile = sheet1.row_values(0)
	global count#定义导入记录的行数
	for i in range(nrows):
		if i == 0: #第一行为标题，跳过
			continue
		row_data = sheet1.row_values(i)#获取excel的每一行
		for n in range(ncol): #对每一行的列进行循环
			if n > 2:#跳过前面固定的三列时间、压力、温度
				rom_id = titile[n]
				if isinstance(row_data[0], str):
					time = row_data[0].replace('/', '-')
				else:
					s_time = xldate_as_tuple(row_data[0],0)
					time = datetime.datetime(*s_time) #时间格式转换
				standard_p = int(row_data[1])
				standard_t = int(float(row_data[2]))
				data = row_data[n].split() #转换为列表
				u = int(data[3],16) #16进制转换为10进制
				uu = pow(u,2)
				t = int(data[2],16)
				ut = u * t
				tt = pow(t,2)
				#下面获取不带后缀文件名，作为批次号码
				(filepath, tempfilename) = os.path.split(file_name)
				(shotname, extension) = os.path.splitext(tempfilename)
				sn = shotname
				raw_code = " ".join(data)
				count = count + 1
				#插入数据库
				models.Raw_data.objects.create(rom_id=rom_id, time=time, standard_p=standard_p, standard_t=standard_t, u=u, uu=uu, t=t, ut=ut, tt=tt, raw_code=raw_code, sn=sn)
	return count


#往数据库导入文件
def add_data(request):
	if request.method == "GET":
		list = os.listdir(r"D:\files")
		acount = 0
		for i in list:
			(shotname, extension) = os.path.splitext(i)
			sn = shotname
			#如果数据库中存在该sn，则跳过不导入
			if_exist = models.Raw_data.objects.filter(sn=sn)
			if if_exist:
				continue
			file_name = os.path.join(r"D:\files", i)
			print(file_name)
			acount = acount + insert_db(file_name)
		return HttpResponse("总记录条数：%d" %count)

#根据搜索条件查询数据
def search(request):
	if request.method == "GET":
		rom_id = request.GET.get("rom_id")
		press = request.GET.get("press")
		temp = request.GET.get("temp")
		sql_dict = dict()
		if rom_id:
			sql_dict['rom_id'] = rom_id
		if press:
			sql_dict['pressure'] = press
		if temp:
			sql_dict['temperature'] = temp
		if sql_dict:
			data_obj = models.Raw_data.objects.filter(**sql_dict)
			p = Paginator(data_obj,10) #分页，10行一页
			if p.num_pages <= 1: #如果内容不足一页
				data_list = data_obj
				data = {} #不需要分页按钮
			else:
				page = int(request.GET.get('page',1)) #获取当前页码，默认为第一页
				data_list = p.page(page) #返回指定页面的内容
				left = [] #当前页左边连续页码号，初始值为空
				right = [] #当前页右边连续的页码号，初始值为空
				left_has_more = False #标识第一页页码后是否需要显示省略号
				right_has_more = False #标识最后一页页码前是否需要显示省略号
				firt = False #是否显示第一页页码
				last = False #标识是否需要显示最后一页的页码
				total_pages = p.num_pages #总页数
				page_range = p.page_range #页码范围，返回一个列表
				if page == 1: #如果是请求第一页
					right = page_range[page:page+2] #获取右边连续页码
					if right[-1] < total_pages -1: #
						right_has_more = True
						if right[-1] < total_pages:
							last = True
				elif page == total_pages: #如果是请求最后一页
					left = page_range[(page-3) if (page-3) > 0 else 0:page - 1] #获取左边连续的页码
					if left[0] > 2:
						left_has_more = True #如果最左边的页码比2大，说明其与第一页之后还有省略号要显示
					if left[0] > 1: #如果最左边的页码比1大，则要显示第一页
						firt = True
				else:#如果请求的页码不是第一页，也不是最后一页
					left = page_range[(page - 3) if (page - 3) > 0 else 0:page -1] #获取左边连续的页码
					right = page_range[page:page+2] #获取右边连续的页码
					if left[0] > 2:
						left_has_more = True
					if left[0] > 1:
						firt = True
					if right[-1] < total_pages -1 :
						right_has_more = True
					if right[-1] < total_pages:
						last = True
				data = {  #将数据包含在字典中
					'left':left,
					'right':right,
					'left_has_more':left_has_more,
					'right_has_more':right_has_more,
					'first':firt,
					'last':last,
					'total_pages':total_pages,
					'page':page
					}
			return render(request, "data_list.html", context={"data_list": data_list,'data':data,'rom_id':rom_id,'press':press,'temp':temp}) #把获取到的get值传回页面，方便分页时通过url可以拿到查询条件
		else: #如果是第一次访问，则所有结果为空，显示空页面
			data_list = ""
			data = {}
			return render(request, "data_list.html", context={"data_list": data_list, 'data': data})

#把求解的系数写入数据库
def regist_data(request):
	engine = create_engine('mysql+pymysql://gtianf:123456.@localhost:3306/dcgc')
	if request.method == "GET":
		rom_id = request.GET.get("rom_id")
		if rom_id:
			if rom_id == 'all':
				s = ""
				rom_ids = models.Raw_data.objects.values_list('rom_id',flat=True).distinct()
				for myid in rom_ids:
					record = models.Tt_coefficient.objects.filter(rom_id=myid)
					# 判断库中是否存在该记录,如果没有则进行计算参数，并导入
					if not record:
						sql = 'select standard_p,standard_t,u,uu,t,ut,tt from app01_raw_data where rom_id="%s"'%(myid)
						data = pd.read_sql_query(sql, engine)
						###针对压力多元回归,带t^2###
						# 选择需要回归的自变量
						u_cols = ['u', 'uu', 't', 'ut', 'tt']
						X = data[u_cols]
						# 需要回归的因变量
						Y = data['standard_p']
						X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0, random_state=1)
						linreg = LinearRegression()
						model = linreg.fit(X_train, Y_train)
						# 获取截距
						a0 = linreg.intercept_
						# 获取系数
						a1, a2, a3, a4, a5 = linreg.coef_
						# 把x值带入系数求解y值
						test_set = linreg.predict(X)
						# 获取残差列表
						ck_list = Y - test_set
						# 平均值
						mean = np.mean(ck_list)
						# 中位数
						median = np.median(ck_list)
						# 方差
						var = np.var(ck_list)
						# 标准差
						std = np.std(ck_list)
						#如果标准差大于1，则存在异常数据，需要进行处理,并标记为不合格
						if std > 1:
							flag = False
							print('带t*t存在异常数据，异常ROM_ID为%s'%(myid))
						else:
							flag = True
						# 协方差
						cov = np.cov(ck_list)
						# 最大值
						max = np.max(ck_list)
						# 最小值
						min = np.min(ck_list)
						# 获取拟合度
						score = linreg.score(X, Y)
						#根据误差情况，对产品进行分级
						percent = (np.sum(ck_list > 0.5) + np.sum(ck_list < -0.5)) / len(list(ck_list))
						if percent <= 0.1:
							level = 1
						elif percent > 0.1 and percent <= 0.2:
							level = 2
						elif percent > 0.2 and percent <= 0.3:
							level = 3
						elif percent > 0.3:
							level = 0
						#针对温度回归
						t_cols = ['t']
						Xt = data[t_cols]
						Yt = data['standard_t']
						Xt_train, Xt_test, Yt_train, Yt_test = train_test_split(Xt, Yt, test_size=0, random_state=1)
						t_linreg = LinearRegression()
						model = t_linreg.fit(Xt_train, Yt_train)
						# 获取截距
						a = t_linreg.intercept_
						# 获取系数
						b = t_linreg.coef_[0]
						# 把残差相关，写入数据库
						#把系数写入数据库
						models.Tt_coefficient.objects.create(rom_id=myid, a0=round(a0,16), a1=round(a1,16), a2=round(a2,16), a3=round(a3,16), a4=round(a4,16), a5=round(a5,16), a=round(a,16), b=round(b,16),\
						mean=mean, median=median, var=var, std=std, cov=cov,max=max, min=min, score=score, level=level,flag=flag)
						s = s + '<h3>设备ID=%s</h3><br> a1=%.16f,a2=%.16f,a3=%.16f,a4=%.16f,a5=%.16f,a=%.16f,b=%.16f <br>' %(myid,a1, a2, a3, a4, a5, a, b)
						### 针对压力多元回归,不带t^2 ###
						# 选择需要回归的自变量
						u_cols = ['u', 'uu', 't', 'ut']
						X = data[u_cols]
						# 需要回归的因变量
						Y = data['standard_p']
						X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0, random_state=1)
						linreg = LinearRegression()
						model = linreg.fit(X_train, Y_train)
						# 获取截距
						a0 = linreg.intercept_
						# 获取系数
						a1, a2, a3, a4 = linreg.coef_
						# 把x值带入系数求解y值
						test_set = linreg.predict(X)
						# 获取残差列表
						ck_list = Y - test_set
						# 平均值
						mean = np.mean(ck_list)
						# 中位数
						median = np.median(ck_list)
						# 方差
						var = np.var(ck_list)
						# 标准差
						std = np.std(ck_list)
						# 如果标准差大于1，则存在异常数据，需要进行处理
						if std > 1:
							flag = False
							print('不带t*t存在异常数据，异常ROM_ID为%s' %(myid))
						else:
							flag = True
						# 协方差
						cov = np.cov(ck_list)
						# 最大值
						max = np.max(ck_list)
						# 最小值
						min = np.min(ck_list)
						# 获取拟合度
						score = linreg.score(X, Y)
						#根据残差，对产品进行分级
						percent = (np.sum(ck_list > 0.5) + np.sum(ck_list < -0.5)) / len(list(ck_list))
						if percent <= 0.1:
							level = 1
						elif percent > 0.1 and percent <= 0.2:
							level = 2
						elif percent > 0.2 and percent <= 0.3:
							level = 3
						elif percent > 0.3:
							level = 0
						# 把残差相关，写入数据库
						models.Coefficient.objects.create(rom_id=myid, a0=round(a0, 16), a1=round(a1, 16), a2=round(a2, 16), a3=round(a3, 16),a4=round(a4, 16), a=round(a, 16), b=round(b, 16),\
						mean=mean, median=median, var=var,std=std, cov=cov, max=max, min=min, score=score, level=level, flag=flag)
						s = s + '不带t*t的系数 <br> a1=%.16f,a2=%.16f,a3=%.16f,a4=%.16f,,a=%.16f,b=%.16f' % (a1, a2, a3, a4, a, b)
			return HttpResponse(s)
		else:
			return HttpResponse("没有传入设备ID")
def test(request):
	pass
def import_data(request):
	return  render(request,'import_data.html')
def project_list(request):
	return render(request, 'project_list.html')



