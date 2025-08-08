from django.urls import path, include
from field_target.competitions import views
from field_target.competitions.views import CompetitionDetailView, CompetitionRegisterView, CompetitionEditView, \
    CompetitionDeleteView

urlpatterns = [
    path('create/', views.CompetitionCreateView.as_view(), name='competition-create'),
    path('all-competitions/', views.ShowAllCompetitionsView.as_view(), name='all-competitions'),
    path('<int:pk>/', include([
        path('details/', CompetitionDetailView.as_view(), name='competition-details'),
        path('register/', CompetitionRegisterView.as_view(), name='competition-register'),
        path('edit/', CompetitionEditView.as_view(), name='competition-edit'),
        path('delete/', CompetitionDeleteView.as_view(), name='competition-delete'),
    ]))
]
