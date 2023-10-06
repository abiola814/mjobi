from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'project'

urlpatterns=[
    path('', views.social_view, name='social_view'),
    path('projects/', views.project_view, name='project_view'),
    path('register/user_register', views.user_register, name='user_register'),
    path('login/user_login', views.user_login, name='user_login'),
    path('register/dashboard/', views.dashboard, name='dashboard'),
    path('login/dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot_password/user_forgot_password', views.forgot_password, name='user_forgot_password'),
    path('password_reset/done', views.password_reset_done, name='password_reset_done'),
        path('chatlogin/', views.chatlogin, name='chatlogin'),
]
