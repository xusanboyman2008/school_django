from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.all, name='all_logins'),
    path('create_login/', views.create_login, name='create_login'),
    path('update_login/<int:pk>/', views.update_login, name='update_login'),
]
