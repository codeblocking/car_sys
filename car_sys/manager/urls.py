from django.conf.urls import url
from manager import views
urlpatterns = [
    url(r'^show/$', views.show),
    url(r'^add/$', views.add),
    url(r'^delete/(?P<id>\d+)/$', views.delete),
    url(r'^reset/(?P<id>\d+)/$', views.reset),

]