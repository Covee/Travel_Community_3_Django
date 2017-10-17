from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

class Post(models.Model):
	title = models.CharField('TITLE', max_length=50)
	imgae = models.ImageField()
	create_date = models.DateTimeField('Create Date', auto_now_add = True)
	modify_date = models.DateTimeField('Modify Date', auto_now = True)

	def __str__(self):
		return self.title


#class Article(models.Model):


