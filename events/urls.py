from django.conf.urls import url

from . import views

app_name = 'events'
urlpatterns = [
    url(r'^new/$', views.events_new, name='events_new'),
    url(r'^stats/$', views.stats, name='stats'),
    
]

