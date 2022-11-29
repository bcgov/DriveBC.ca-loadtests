from apps.api.route_planner.permissions import IsAdminOrReadOnly
from apps.api.route_planner.serializers import TravelAdvisoryMessageSerializer
from apps.route_planner.models import TravelAdvisoryMessage
from rest_framework import viewsets


class TravelAdvisoryMessageViewSet(viewsets.ModelViewSet):
    """ """

    queryset = TravelAdvisoryMessage.objects.all()
    serializer_class = TravelAdvisoryMessageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            return qs.filter(pub_date__isnull=False)
        return qs
