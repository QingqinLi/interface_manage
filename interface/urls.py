# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf.urls import url
from interface import views

urlpatterns = [
    url(r'^index/', view=views.index, name='index'),
    url(r'^msg/', view=views.msg_interface, name='interface_msg'),
    url(r'^add/', view=views.add_interface, name='interface_add'),
    url(r'^show/(?P<page>\d+)', view=views.show_interface, name='interface_show'),
    url(r'^del/(?P<case_id>\d+)', view=views.del_interface, name='interface_del'),
]