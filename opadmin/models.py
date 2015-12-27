# coding:utf-8
from django.db import models

# Create your models here.

class ServerFunCateg(models.Model):
	id = models.IntegerField(primary_key=True, db_column='ID')
	server_categ_name = models.CharField(max_length=60)
	delmark = models.CharField(max_length=10, default='N')	#default='Y' 表示记录删除
	class Meta:
		db_table = u'server_fun_categ'

class ServerAppCateg(models.Model):
	id = models.IntegerField(primary_key=True, db_column='ID')
	server_categ_id = models.IntegerField()
	app_categ_name = models.CharField(max_length=90)
	delmark = models.CharField(max_length=10, default='N')
	class Meta:
		db_table = u'server_app_categ'

class ServerHostList(models.Model):
	server_host_name = models.CharField(max_length=40, primary_key=True)
	server_host_wip = models.CharField(max_length=45)
	server_host_nip = models.CharField(max_length=45)
	server_host_os = models.CharField(max_length=30)
	server_app_id = models.IntegerField()
	delmark = models.CharField(max_length=10, default='N')
	class Meta:
		db_table = u'server_host_list'

class ModuleList(models.Model):
	id = models.IntegerField(primary_key=True, db_column='ID')
	module_name = models.CharField(max_length=60)
	module_caption = models.CharField(max_length=800)
	module_extend = models.CharField(max_length=6000)
	delmark = models.CharField(max_length=10, default='N')
	class Meta:
		db_table = u'module_list'
