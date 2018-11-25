from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import xlrd
import datetime
from xlrd import xldate_as_tuple
import os
# Create your views here.
count = 0
def insert_db(file_name):
	book = xlrd.open_workbook(file_name)
	sheet1 = book.sheet_by_index(0)
	nrows = sheet1.nrows
	ncol = sheet1.ncols
	titile = sheet1.row_values(0)
	global count
	for i in range(nrows):
		if i == 0: #第一行为标题，跳过
			continue
		row_data = sheet1.row_values(i)#获取excel的每一行
		for n in range(ncol):
			if n > 2:#跳过前面固定的三列时间、压力、温度
				rom_id = titile[n]
				s_time = xldate_as_tuple(row_data[0],0)
				time = datetime.datetime(*s_time) #时间格式转换
				press = row_data[1]
				temp = row_data[2]
				data = row_data[n].split() #转换为列表
				s_volt = int(data[0],16)/16
				s_press = int(data[2],16) #16进制转换为10进制
				s_temp = int(data[3],16)
				s_data = " ".join(data)
				count = count + 1
				#插入数据库
				models.Raw_data.objects.create(rom_id=rom_id,time=time,pressure=press,temperature=temp,s_volt=s_volt,s_press=s_press,s_temp=s_temp,s_data=s_data)
	return count


#往数据库导入文件
def add_data(request):
	if request.method == "GET":
		list = os.listdir(r"D:\files")
		count_list = []
		for i in list:
			file_name = os.path.join(r"D:\files", i)
			print(file_name)
			acount = insert_db(file_name)
			count_list.append(",")
			count_list.append(acount)
		return HttpResponse(count_list)

#根据搜索条件查询数据
def search(request):
	if request.method == "GET":
		return render(request, "search.html")
	if request.method == "POST":
		rom_id = request.POST.get("rom_id")
		press = request.POST.get("press")
		temp = request.POST.get("temp")
		r_s = ""
		p_s = ""
		t_s = ""
		print(rom_id)
		if rom_id:
			r_s = "rom_id=%s," %rom_id
			print(r_s)
		if press:
			p_s = "pressure=%s," %press
			print(p_s)
		if temp:
			t_s = "temperature=%s, " %temp
			print(t_s)

		s_sql = r_s + p_s + t_s
		print(s_sql)
		str(s_sql)[:-1]
		print(s_sql)

		data_obj = models.Raw_data.objects.filter(s_sql)
		return render(request, "data_list.html", {"data": data_obj})


def test(request):
	pass


