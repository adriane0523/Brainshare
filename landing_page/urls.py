from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('narrative/', views.about, name='about'),
    path('aims/', views.about_aims, name='about_aims'),
    path('about-john-sulston/', views.about_sulston, name='about_sulston'),
    path('importance/', views.about_importance, name='about_importance'),
    path('modified-policy-delphi/', views.about_modified_delphi, name ="about_MDP"),
    path('contact/', views.contact, name="contact"),
    path('terms-and-conditions/', views.terms_cond, name ="terms_cond"),
    path ('privacy/', views.privacy, name="privacy"),
    path('citations/', views.citations, name = "citations"),
    
]