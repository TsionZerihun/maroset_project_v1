from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashbaord, name='dashboard'),
    path('apply', views.apply, name='apply'),
    path('applied-jobs', views.applied, name='applied'),
    path('My-Posted-Jobs', views.jobs, name='jobs'),
    path('company', views.company, name='company')



]