from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('form1/', views.form1test.as_view(), name ='form1'),
    path('form2/', views.r80apitest.as_view(), name='form2')
]