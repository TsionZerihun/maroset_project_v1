from django.urls import path
from . import views
urlpatterns = [
    path('register-applicant/', views.register_applicant, name='register-applicant'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('blocked/', views.blocked, name='blocked')


]