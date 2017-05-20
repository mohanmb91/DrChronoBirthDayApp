from django.conf.urls import include, url
from django.views.generic import TemplateView

import views

import secretkeys;

clientid = secretkeys.client_id;
urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    #url(r'^$', views.get_access),
    url(r'^$', views.get_access,name = "cId"),
    url(r'^home/$' , views.get_home, name='home'),
    url(r'^home/wishpatient/(?P<id>\d+)/$', views.wishpatient),

    #url(r'', include('social.apps.django_app.urls', namespace='social')),
]