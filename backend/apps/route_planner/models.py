from apps.shared.models import BaseModel
from django.contrib.auth.models import User
from django.db import models


class TravelAdvisoryMessage(BaseModel):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(null=True, blank=True)
