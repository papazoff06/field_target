from django.urls import path

from field_target.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
]