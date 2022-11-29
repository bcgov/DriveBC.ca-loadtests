from django.urls import include, path

from .route_planner import urls as route_planner_urls

urlpatterns = [
    path("", include(route_planner_urls)),
]
