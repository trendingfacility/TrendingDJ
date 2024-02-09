# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('profile', views.getProfile),
    path('Dashboard', views.Dashboard),
    path('icons', views.getIcons),
    path('map', views.getMaps),
    path('tables', views.getTables),


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
