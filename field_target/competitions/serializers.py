from rest_framework import serializers

from field_target.competitions.models import Competition


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
