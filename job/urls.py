from django.urls import path
from .views import *



urlpatterns = [
    path('jobs/', getAllJobs, name='getAllJobs'),
    path('jobs/<int:pk>/', getJob, name='getJob'),
    path('jobs/new/', new_job, name='new_job'),
    path('jobs/update/<int:pk>/', update_job, name='update_job'),
    path('jobs/delete/<int:pk>/', delete_job, name='delete_job'),
    path('jobs/<str:topic>', getTopicStats, name='get_topic_stats'),
    ]