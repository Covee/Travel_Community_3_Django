from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

class Post(models.Model):
	title = models.CharField('TITLE', max_length=50)
	#image = models.ImageField( upload_to=user_directory_path, )
	#country = models.CharField()
	create_date = models.DateTimeField('Create Date', auto_now_add = True)
	modify_date = models.DateTimeField('Modify Date', auto_now = True)

	def __str__(self):
		return self.title


class BoardList(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	create_date = models.DateTimeField('Create Date', auto_now_add = True)
	clicks = models.IntegerField(default=0)
	owner_rate = 


class HomeBestPhoto(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100, blank=True)

	class Meta:
		ordering = ['-create_date']

	def __str__(self):
		return self.name


class HomeBestBoard(models.Model):
	name = models.CharField(max_length=50)
	clicks = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)







