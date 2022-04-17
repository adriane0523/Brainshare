from django.urls import path
from . import views

urlpatterns = [
    path('', views.resources, name='resources'),
    path('<int:id>/', views.resource_index, name='resource_index'),
    path('case-study/<uuid>/', views.case_study, name='case_study'),
    path('related_projects/', views.related_projects, name='related_projects'),
    path('publications/', views.publications, name='publications'),
    path('white-papers', views.white_papers, name="white_papers"),
    path('relevant_docs', views.relevant_docs, name="relevant_docs"),
    path('patient_stories', views.patient_stories, name="patient_stories"),
    path('patient_stories/<uuid>', views.patient_stories_index, name="patient_stories_index")           
    
]