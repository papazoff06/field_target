from rest_framework.routers import DefaultRouter

from .api_views import CompetitionViewSet

from django.urls import path, include

router = DefaultRouter()
router.register(r'competitions', CompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
