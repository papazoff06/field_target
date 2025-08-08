from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Competition
from .serializers import CompetitionSerializer


class AdminPermissionOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [AdminPermissionOnly]
