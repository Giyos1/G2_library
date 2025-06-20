from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    # path("file_upload/", views.file_upload, name='file_uploads'),
    # path("file_list/", views.file_list, name='file_list'),
    # path('forgot_password/', views.ForgotPassword.as_view(), name='forgot_password'),
    # path('restore_password', views.RestorePassword.as_view(), name='restore_password')
]
