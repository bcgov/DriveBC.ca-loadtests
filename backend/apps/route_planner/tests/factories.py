import datetime
import random
import factory
from factory import fuzzy
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, LineString
from factory.fuzzy import BaseFuzzyAttribute

from app.route_planner.models import (
    TravelAdvisoryMessage,
    Route,
)

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    email = "admin@gmail.com"
    username = "admin"
    password = None

class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0))


class TravelAdvisoryMessageFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("title")
    text = factory.Faker("text")
    author = factory.SubFactory(UserFactory)
    pub_date = factory.LazyFunction(datetime.now)

    class Meta:
        model = TravelAdvisoryMessage


class RouteFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    start_point = FuzzyPoint
    destination_point = FuzzyPoint
    route_points = LineString(FuzzyPoint, FuzzyPoint)
    criteria = factory.fuzzy.FuzzyChoice(
        [choice[0] for choice in Route.CRITERIA_CHOICES]
    )
    srs_code = "34567"
    distance_unit = factory.fuzzy.FuzzyChoice(
        [choice[0] for choice in Route.DISTANCE_UNIT_CHOICES]
    )
    distance = factory.fuzzy.FuzzyFloat()
    route_time = factory.fuzzy.FuzzyFloat()


    class Meta:
        model = Route
