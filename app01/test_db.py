# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dcgc.settings")
import django
django.setup()
from app01 import db


sql = "select * from ProjectTree limit 10"
ms = db.MySql()
res_list = ms.ExecQuery(sql)
for row in res_list:
	print(row)