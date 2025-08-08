from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from field_target.sponsors.models import Sponsor
from field_target.sponsors.serializers import SponsorSerializer


# Create your views here.
class SponsorListView(ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer