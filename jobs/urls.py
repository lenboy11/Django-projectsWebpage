from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name="job-home"),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name="job-detail"),
    path('update/', views.jobUpdate, name="job-update"),
]
