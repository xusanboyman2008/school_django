from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name='all_logins'),  # Display the table
    path('create_login/', views.create_login, name='create_login'),  # Create a login
    path('update_login/<int:pk>/', views.update_login, name='update_login'),  # Update a login
]
