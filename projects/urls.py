from django.conf.urls import include,url
from . import views

urlpatterns = [
	url(r'^$',views.project_list, name="list"),
	url(r'(?P<pk>\d+)/$',views.project_detail,name='detail')
	#url(r'^posts/',views.post_list,name="posts") , #posts/
]

