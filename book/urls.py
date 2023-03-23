__author__ = 'Administrator'

from django.contrib import admin
from django.urls import path,re_path
from book import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('select_book/',views.select_book),
    re_path('select_books/(\d+)/delete/',views.delbook),
    re_path('update_books/(\d+)/update/',views.upbook),
    path('add/',views.add_duo),
    path('select/',views.se),
    re_path('duo_add/',views.duo_add),
    re_path('s_book/',views.s_book),
    re_path('book_up/(\d+)/change/$',views.change),
    re_path('book_de/(\d+)/shanchu/$',views.shanchu),



]
