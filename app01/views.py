from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import xlrd
import datetime
from xlrd import xldate_as_tuple
import os
from django.core.paginator import Paginator
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
				volt = round(s_volt,1)
				s_press = int(data[2],16) #16进制转换为10进制
				s_temp = int(data[3],16)
				s_data = " ".join(data)
				count = count + 1
				#插入数据库
				models.Raw_data.objects.create(rom_id=rom_id,time=time,pressure=press,temperature=temp,s_volt=volt,s_press=s_press,s_temp=s_temp,s_data=s_data)
	return count


#往数据库导入文件
def add_data(request):
	if request.method == "GET":
		list = os.listdir(r"D:\files")
		acount = 0
		for i in list:
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


def test(request):
	pass


