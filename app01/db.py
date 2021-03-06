# -*- coding:utf-8 -*-
import pymysql
from app01 import config

class MySql:
	def __init__(self):
		self.host = config.HOST
		self.user = config.USER
		self.pwd = config.PWD
		self.db = config.DB
		self._conn = self.GetConnect()
		if (self._conn):
			self._cur = self._conn.cursor()

	#连接数据库
	def GetConnect(self):
		conn =False
		try:
			conn = pymysql.connect(
				host = self.host,
				user = self.user,
				password = self.pwd,
				database = self.db
			)
		except Exception as err:
			print("连接数据库失败，%s" % err)
		else:
			return conn

	#执行查询
	def ExecQuery(self,sql):
		res = ""
		try:
			self._cur.execute(sql)
			res = self._cur.fetchall()
		except Exception as err:
			print("查询失败，%" %err)
		else:
			return res
	#执行非查询类语句
	def ExecNonQuery(self,sql):
		flag = False
		try:
			self._cur.execute(sql)
			self._conn.commit()
			flag = True
		except Exception as err:
			flag = False
			self._conn.rollback()
			print("执行失败，%s" %err)
		else:
			return flag

	#获取连接信息
	def GetConnectInfo(self):
		print("连接信息：")
		print("服务器：%s,用户名：%s,数据库：%s" %(self.host,self.user,self.db))

	#关闭数据库连接
	def Close(self):
		if (self._conn):
			try:
				if (type(self._cur) == 'object'):
					self._cur.close()
				if (type(self._conn) == 'object'):
					self._conn.close()
			except:
				raise ("数据库连接关闭异常，%s,%s" %s(type(self._cur, type(self._conn))))


