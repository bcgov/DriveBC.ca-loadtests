from apps.route_planner.models import TravelAdvisoryMessage
from rest_framework import serializers


class TravelAdvisoryMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAdvisoryMessage
        fields = ("id", "text", "author", "pub_date", "created_at", "modified_at")
