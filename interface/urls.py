# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf.urls import url
from interface import views

urlpatterns = [
    url(r'^index/', view=views.index, name='index')
]