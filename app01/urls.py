__author__ = 'Administrator'


from django.contrib import admin
from django.urls import path,re_path

from  app01 import  views


urlpatterns = [
    path('timer/', views.timer),
    re_path(r'^articles/2003/$', views.special_case_2003),#路由配置
    re_path(r'^articles/([0-9]{4})/$',views.arivch_year),
    #re_path(r'^articles/([0-9]{4})/([0-9]{2})/$',views.arivch_year_moth),
    #有名分组
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$',views.arivch_year_moth),
    path('ajx/',views.ajx),
    path('test_ajx/',views.test_ajx),
    path('cal/',views.cal),
    path('login/',views.login),
    path('fy/',views.fy)

]
