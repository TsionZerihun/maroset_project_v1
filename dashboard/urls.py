from django.urls import path
from . import views
from job.views import all_applicant


urlpatterns = [
    path('', views.dashbaord, name='dashboard'),
    path('apply', views.apply, name='apply'),
    path('applied', views.applied, name='applied'),

    path('My-Posted-Jobs', views.jobs, name='jobs'),
    path('company', views.company, name='company'),
    path('chat_admin/<int:pk>/', views.user_with_admin_chat, name='user_with_admin_chat'),

    path('admin', views.admin_index, name='administrator'),
    path('admin/jobs', views.admin_jobs, name='admin_jobs'),
    path('admin/users', views.admin_view_users, name='admin_users'),
    path('admin/reported', views.admin_reported_jobs, name='admin_reported'),
    path('admin/job_response/<int:pk>/', views.admin_response, name='admin_response'),
    path('admin/admin_block/<int:pk>/', views.block_users, name='block_users'),
    path('admin/admin_unblock/<int:pk>/', views.unblock_users, name='unblock_users'),
    path('admin/admin_message_job/<int:pk>/', views.message_job, name='job-messages'),
    path('chat/<int:pk>/', views.user_message_job, name='job-owner-messages'),
    path('admin/messages', views.admin_chat_users, name='admin_messages'),
    path('admin/personal_chat/<int:pk>/', views.admin_with_one_user_chat, name='chat_specific_user'),
    path('admin/logout', views.logout_admin, name='admin_logout')


















]