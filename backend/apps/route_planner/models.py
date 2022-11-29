from django.contrib import admin
from django.utils import timezone

from apps.shared.models import BaseModel
from django.contrib.auth.models import User
from django.db import models


class TravelAdvisoryMessage(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name="Publication date", null=True,
                                    blank=True)

    class Meta:
        verbose_name = "Travel Advisory Message"

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Is published',
    )
    def is_published(self):
        now = timezone.now()
        return self.pub_date is not None and self.pub_date <= now
