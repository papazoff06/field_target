from django.urls import path, include
from field_target.competitions import views
from field_target.competitions.views import UpdateScoresView

urlpatterns = [
    path('create/', views.CompetitionCreateView.as_view(), name='competition-create'),
    path('all-competitions/', views.ShowAllCompetitionsView.as_view(), name='all-competitions'),
    path('competition-history', views.ShowPastCompetitionsView.as_view(), name='competition-history'),
    path('<int:pk>/competition-history', views.PastCompetitionDetailView.as_view(), name='competition-details'),
    path('<int:competition_id>/update-scores/', UpdateScoresView.as_view(), name='update-scores'),
    path('<int:pk>/', include([
        path('details/', views.CompetitionDetailView.as_view(), name='competition-details'),
        path('register/', views.CompetitionRegisterView.as_view(), name='competition-register'),
        path('edit/', views.CompetitionEditView.as_view(), name='competition-edit'),
        path('delete/', views.CompetitionDeleteView.as_view(), name='competition-delete'),
    ])),
]
