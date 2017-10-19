from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from board import views

urlpatterns = [
	url(r'^$', views.KoreaBoard(template_name='Korea/Board.html')),
	url(r'^(?P<pk>\d+)/$', 'views.Post_detail'),
	url(r'^new/$', 'views.Post_New'),
	url(r'^(?P<pk>\d+)/Comments/new/$', 'views.Comment_new')  # 댓글 생성
	url(r'^(?P<post_pk>\d+)/Comments/(?P<pk>\d+)/edit/$', 'views.Comment_edit')  # 댓글 수정
	url(r'^$', views.EastAsiaBoard(template_name='East_Asia/Board.html')),
	url(r'^$', views.EuropeBoard(template_name='Europe/Board.html')),
	url(r'^$', views.NorthAmericaBoard(template_name='North_America/Board.html')),
	url(r'^$', views.SouthAmericaBoard(template_name='South_America/Board.html')),
	url(r'^$', views.AustrailiaBoard(template_name='Austrailia/Board.html')),
	url(r'^$', views.AfricaBoard(template_name='Africa/Board.html')),
	url(r'^$', views.FreeBoard(template_name='FreeBoard.html')),
#    url(r'^$', BoardList.as_view(template_name='board.html')),
#    url(r'^$', BoardList.as_view(template_name='board_detail.html')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
