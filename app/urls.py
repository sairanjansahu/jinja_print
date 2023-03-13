from app.views import *
from django.urls import path
app_name='a'
urlpatterns=[
    path('jinja_print/',jinja_print,name='jinja_print'),
]