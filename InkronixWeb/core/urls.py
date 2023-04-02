from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('team/',Team.as_view(),name='team'),
    path('we_do/',WhatWeDo.as_view(),name='we_do'),
    path('admin_login/',AdminLogin.as_view(),name='admin_login'),
  
]
