from django.urls import path
from . import views

urlpatterns = [
    path('create-company/', views.create_company, name='create_company'),
    path('create-startup/', views.create_startup, name='create_startup'),
    path('company-details/<int:pk>/', views.company_details, name='company_details'),
    path('startup-details/<int:pk>/', views.startup_details, name='startup_details'),
    path('update-startup/<int:pk>/', views.update_startup, name='update_startup'),
    path('update-company/<int:pk>/', views.update_company, name='update_company')

]