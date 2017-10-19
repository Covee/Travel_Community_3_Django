from django.conf.urls import url, include
from django.contrib import admin

from Travel_Comm.views import HomeView
from .board.views import KoreaBoard 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('board.urls')),
    url(r'^$', HomeView.as_view(template_name='index.html')),
]
