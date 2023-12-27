from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name= 'create-job') ,
    path('update-job/<int:pk>/', views.Update_job, name='update-job'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('all-applicants/<int:pk>/', views.all_applicant, name='all-applicants')



]