from django.db import models

# Create your models here.
# class SoftTest(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	rom_id = models.CharField(max_length=30, null=False)
# 	intercept = models.CharField(max_length=20)
# 	p = models.CharField(max_length=20)
# 	p_p = models.CharField(max_length=20)
# 	t = models.CharField(max_length=20)
# 	t_p = models.CharField(max_length=30)
# 	a = models.CharField(max_length=20)
# 	b = models.CharField(max_length=20)
# 	min_range = models.IntegerField()
# 	max_range = models.IntegerField()
# 	min_temperature = models.IntegerField()
# 	max_temperature = models.IntegerField()
# 	level = models.CharField(max_length=30)
# 	g = models.CharField(max_length=20)
# 	temperature = models.IntegerField()

#定义源基础数据表
class Raw_data(models.Model):
	id = models.AutoField(primary_key=True)
	rom_id = models.CharField(max_length=30, null=False)
	time = models.DateTimeField()
	pressure = models.IntegerField()
	temperature = models.IntegerField()
	s_volt = models.FloatField()
	s_press = models.IntegerField()
	s_temp = models.IntegerField()
	s_data = models.CharField(max_length=30)