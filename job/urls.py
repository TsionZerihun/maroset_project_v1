from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name= 'create-job') ,
    path('update-job/<int:pk>/', views.Update_job, name='update-job'),
    path('admin-update-job/<int:pk>/', views.admin_Update_job, name='admin_update-job'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('all-applicants/<int:pk>/', views.all_applicant, name='all-applicants'),
    path('report_job/<int:pk>/', views.report_job, name='report-job'),
    path('report_detail/<int:pk>/', views.report_job_reason, name='report-detail'),
    path('job_report_detail/<int:pk>/', views.about_reported_job, name='about-report-detail')






]