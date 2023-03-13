from django.urls import path
from rcb.views import *
app_name='something'
urlpatterns=[
    path('virat/',virat,name='virat')
]
