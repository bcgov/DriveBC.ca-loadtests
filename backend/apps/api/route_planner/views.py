from apps.api.route_planner.permissions import IsAdminOrReadOnly
from apps.api.route_planner.serializers import TravelAdvisoryMessageSerializer
from apps.drivebc_api.drivebc_client import DrivebcClient
from apps.route_planner.models import TravelAdvisoryMessage
from django.http import JsonResponse
from rest_framework import views, viewsets


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


class WebcamDataAPIView(views.APIView):
    """Retrieve webcam data from Drive BC API"""

    def get(self, request, *args, **kwargs):
        webcam_data = DrivebcClient().get_webcams()
        return JsonResponse(data=webcam_data)
