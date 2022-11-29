from apps.api.route_planner.views import TravelAdvisoryMessageViewSet, WebcamDataAPIView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    "travel-advisory-messages",
    TravelAdvisoryMessageViewSet,
    basename="travel-advisory-message",
)

urlpatterns = [
    path(
        "webcams",
        WebcamDataAPIView.as_view(),
        name="webcams",
    ),
    path("", include(router.urls)),
]
