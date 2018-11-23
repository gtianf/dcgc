from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import xlrd

# Create your views here.
def insert_db(file_name):
	#file = r"D:\kqj\416、DEGC-S0820(36）校准报告.xlsx"
	book = xlrd.open_workbook(file_name)
	sheet1 = book.sheet_by_index(1)
	sheet_name = book.sheet_names()[1]
	#print(sheet_name)
	nrows = sheet1.nrows
	t_list = ["rom_id","intercept","p","p_p","t","t_p","a","b","min_range","max_range","min_temperature","max_temperature","level","g","temperature"]
	for i in range(nrows):
		if i == 0: #如果是表头，则跳过
			continue
		ncols = sheet1.ncols
		for n in range(ncols):
			t_list[n] = sheet1.cell_value(i,n)
		models.SoftTest.objects.create(intercept=t_list[0],p=t_list[1],p_p=t_list[2],t=t_list[3],t_p=t_list[4],a=t_list[5],b=t_list[6],min_range=t_list[7],max_range=t_list[8],min_temperature=t_list[9],max_temperature=t_list[10],level=t_list[11],g=t_list[12],temperature=t_list[13])

# list = os.listdir(r"D:\kqj")
# for file in list:
# 	file_name = r"D:\kqj\%s" %file
# 	insert_db(file_name)
def add_data(request):
	insert_db(r"D:\kqj\416、DEGC-S0820(36）校准报告.xlsx")
	return HttpResponse("OK")

