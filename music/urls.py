from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns= [
    url(r'^$' , views.index),

    url(r'^form/$', views.detail, name='detail'),
    url(r'^submit/$', views.submit, name='submit'),
]