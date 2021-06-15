from django.conf.urls import include, url
from . import views
from blog import views
from blog.views import ReceptionView, AjaxDoctorView, SpecializationList, DoctorList
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^about/$', views.about, name='about'),
    url(r'^patient/$', views.patient, name='patient'),
    url(r'^contact/$', views.contactform, name='contact'),
	url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^ajax_get_doctor/$', AjaxDoctorView.as_view(), name='ajax_get_doctor'),
    url(r'^date_from_ajax/$', views.date_from_ajax, name='date_from_ajax'),
    url(r'^spec/(?P<specialization>\d+)/reception/(?P<doctor>\d+)/$', ReceptionView.as_view(), name='reception'),
    url(r'^spec/$', SpecializationList.as_view(), name='spec'),
    url(r'^spec/(?P<specialization>\d+)/$', views.doctorsList, name='vrach'), 
    url(r'^specializationsSelectHandler/$', views.specializationsSelectHandler, name='specializationsSelectHandler'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog')
]