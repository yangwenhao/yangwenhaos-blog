from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^page/(\d+)/$', views.page, name='page'),
    url(r'^(\d{4})/(\d{1,2})/(\d{1,2})/([^/]+)/$', 
        views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
)
