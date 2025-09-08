from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('skills/', views.skills_view, name='skills'),
    path('skills/hard/', views.skills_view, {'type':'hard'}, name='hard_skills'),
    path('skills/soft/', views.skills_view, {'type':'soft'}, name='soft_skills'),
    path('projects/', views.projects_view, name='projects'),
    path('certifications/', views.certifications_view, name='certifications'),
    path('certifications/upload/', views.upload_certification, name='upload_certification'),  # admin-only upload
]
