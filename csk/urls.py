from django.urls import path
from csk.views import *
app_name='something'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]