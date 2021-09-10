from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name="projects-home"),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name="project-detail"),
    path('project/create/', views.ProjectCreateView.as_view(), name="project-create"),
    path('project/<int:pk>/edit', views.ProjectUpdateView.as_view(), name="project-edit"),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name="project-delete"),
    path('about/', views.about, name="projects-about"),
    path('link/', views.LinkListView.as_view(), name="link-home"),
    path('link/<int:pk>/', views.LinkDetailView.as_view(), name="link-detail"),
    path('link/create/', views.LinkCreateView.as_view(), name="link-create"),
    path('link/<int:pk>/edit', views.LinkUpdateView.as_view(), name="link-edit"),
    path('link/<int:pk>/delete', views.LinkDeleteView.as_view(), name="link-delete"),
]
