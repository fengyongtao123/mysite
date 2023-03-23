"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include,register_converter

from  blog import  views

from app01.urlconvert import  mon_convert

register_converter(mon_convert,"mm") #自定义转换器
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('timer/', views.timer),
    path('login/',views.login,name='Log'), #反向解析
    # re_path(r'^articles/2003/$', views.special_case_2003),#路由配置
    # re_path(r'^articles/([0-9]{4})/$',views.arivch_year),
    # #re_path(r'^articles/([0-9]{4})/([0-9]{2})/$',views.arivch_year_moth),
    # #有名分组
    # re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$',views.arivch_year_moth)

    #路由控制分发
    re_path(r'^app01/',include(('app01.urls','app01'))), #命名空间

    #path('articles/<path:year>',views.path_year),
    path('articles/<mm:month>',views.path_month), #自定义转换器
    path('index/',views.index,name="index1"),
    # path('base/',views.base,name="base"),
    path('db/',views.db,name="db"),
    re_path(r'^book/',include(('book.urls','book'))),


]
