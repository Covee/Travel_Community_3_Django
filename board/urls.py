from django.conf.urls import url, include

from Travel_Comm.views import *

urlpatterns = [
    url(r'^$', BoardList.as_view(template_name='board.html')),
    url(r'^$', BoardList.as_view(template_name='board_detail.html')),

    
]
