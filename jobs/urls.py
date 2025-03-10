from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/create/', views.job_create, name='job_create'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
]
