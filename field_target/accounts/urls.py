from django.urls import path

from field_target.accounts import views
from field_target.accounts.views import ProfileDetailsView

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileDetailsView.as_view(), name='profile-details'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]