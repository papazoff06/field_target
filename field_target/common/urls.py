from django.urls import path
from field_target.common import views

urlpatterns = [
    path('', views.ShowHomePageView.as_view(), name='home'),
    path('calculator/', views.ShowCalculatorPageView.as_view(), name='calculator')
]