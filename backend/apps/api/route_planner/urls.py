from apps.api.route_planner.views import TravelAdvisoryMessageViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    "travel-advisory-messages",
    TravelAdvisoryMessageViewSet,
    basename="travel-advisory-message",
)

urlpatterns = [
    path("", include(router.urls)),
]
