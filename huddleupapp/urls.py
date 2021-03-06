from django.conf.urls import url
from . import views

app_name = "huddleupapp"

urlpatterns = [
    # ex: /huddleupapp/
    url(r'^$', views.index, name='index'),
    url(r'^about', views.aboutus, name='aboutus'),
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^tutorial', views.tutorial, name='tutorial'),
    url(r'^mycalendar', views.mycalendar, name='mycalendar'),

    # ex: /huddleupapp/1/
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),

]
