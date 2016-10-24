from django.conf.urls import include,url
from . import views

urlpatterns = [
	url(r'^$',views.project_list, name="list"),
	url(r'^create/$', views.project_create),
	url(r'(?P<pk>\d+)/$',views.project_detail,name='detail'),
    url(r'(?P<pk>\d+)/edit/$', views.project_update, name="update"),
    url(r'^delete/$', views.project_delete),
]

