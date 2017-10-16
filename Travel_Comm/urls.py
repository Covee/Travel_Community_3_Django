from django.conf.urls import url, include
from django.contrib import admin

from Travel_Comm.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(template_name='index.html')),
    #url(r'^)
]
