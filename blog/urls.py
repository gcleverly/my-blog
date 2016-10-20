from django.conf.urls import include,url
from . import views

urlpatterns = [
	url(r'^$',views.post_list, name="list"),
    url(r'^create/$', views.post_create),
    url(r'(?P<pk>\d+)/$', views.post_detail, name='detail'),
    url(r'(?P<pk>\d+)/edit/$', views.post_update,name="update"),
    url(r'^delete/$', views.post_delete)
	#url(r'^posts/',views.post_list,name="posts") , #posts/
]

