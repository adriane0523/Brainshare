from django.urls import path
from bio import views

urlpatterns = [
    path('', views.bio, name='bio'),
    path('co_principal/<int:id>', views.Co_Principal_Investigators_bio, name = "Co_Principal_Investigators_bio"),
    path('co/<int:id>', views.Co_Investigators_bio, name = "Co_Investigators_bio"),
    path('project_personnel/<int:id>', views.Project_Personnel_bio, name = "project_personnel_bio"),
    path('advisory_comitee/<int:id>', views.Advisory_Comitee_bio, name = "advisory_comitee_bio"),
]