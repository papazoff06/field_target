from django.urls import path
from field_target.competitions import views
from field_target.competitions.views import CompetitionDetailView, CompetitionRegisterView, CompetitionEditView

urlpatterns = [
    path('create/', views.CompetitionCreateView.as_view(), name='competition-create'),
    path('all-competitions/', views.ShowAllCompetitionsView.as_view(), name='all-competitions'),
    path('<int:pk>/details', CompetitionDetailView.as_view(), name='competition-details'),
    path('<int:pk>/register/', CompetitionRegisterView.as_view(), name='competition-register' ),
    path('<int:pk>/edit/', CompetitionEditView.as_view(), name='competition-edit')
]