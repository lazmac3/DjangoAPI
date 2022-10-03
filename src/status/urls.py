# myapp/urls.py This file is in the myapp folder!
from . import views
from django.urls import path
urlpatterns = [
 path('helloworld/', views.myapp_hi, name='status'),
 path('viewstatus/',views.piazza_status, name='status'),

]
