from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from django.contrib import  admin
import views

import secretkeys;

admin.autodiscover();

clientid = secretkeys.client_id;
urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    #url(r'^$', views.get_access),
    url(r'^$', views.get_access,name = "cId"),
    url(r'^home/$' , views.get_home, name='home'),
    url(r'^home/wishpatient/(?P<id>\d+)/$', views.wishpatient,name = "wishPatient"),
    url(r'^home/sendemail',views.sendEmail),
    url(r'^admin/',include(admin.site.urls)),
    #url(r'', include('social.apps.django_app.urls', namespace='social')),
]