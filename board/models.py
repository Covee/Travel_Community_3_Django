from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


# 메인페이지, 각 게시판 별 OOO BestBoard로 명칭
# 게시형태 = 글 제목[댓글수] / 조회수
class KoreaBestBoard(models.Model):
	name = models.CharField(max_length=50)
	clicks = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)


class EastAsiaBestBoard(models.Model):



class EuropeBestBoard(models.Model):
	


class NorthAmericaBestBoard(models.Model):
	


class SouthAmericaBestBoard(models.Model):



class AustrailiaBestBoard(models.Model):
	


class AfricaBestBoard(models.Model):
	


# 메인페이지 주간 베스트 포토후기 모음 (UI 인스타 형식으로) 
class WeeklyBestPhoto(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100, blank=True)

	class Meta:
		ordering = ['-create_date']

	def __str__(self):
		return self.name

# 가로 광고(랜덤함수 적용)
class ADViewHZ(models.Model):
	image = 


# 세로 광고(랜덤함수 적용)
class ADViewVC(models.Model):
	image = 


# 게시판뷰(글 목록)
class BoardList(models.Model):
	city_country =
	thumbnail_view = 
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	create_date = models.DateTimeField('Create Date', auto_now_add = True)
	clicks = models.IntegerField(default=0)
	owner_rate = 
	search = 


# 일별 댓글, 조회수, 평점 순위 리스트 모델
class DailyBestComment(models.Model):


class DailyBestClick(models.Model):


class DailyBestRate(models.Model):



# 게시글 뷰 모델
class Post(models.Model):
	# id = PositiveIntegerField(), primary_key
	title = models.CharField('TITLE', max_length=50)
	author = models.ForeignKey()
	image = models.ImageField(blank=True, null=True)
	city_country = 
	content = models.TextField('CONTENT', blank=True)
	create_date = models.DateTimeField('Create Date', auto_now_add = True)
	modify_date = models.DateTimeField('Modify Date', auto_now = True)

	def __str__(self):
		return self.title


# 댓글기능 모델
class Comments(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=1000, blank=False)
	author = models.ForeignKey()
	create_date = models.DateTimeField('Create Date', auto_now_add = True)
	modify_date = models.DateTimeField('Modify Date', auto_now = True)






