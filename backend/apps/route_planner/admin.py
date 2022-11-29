from django.contrib import admin

from .models import TravelAdvisoryMessage


class TravelAdvisoryMessageAdmin(admin.ModelAdmin):
    list_display = ("text", "pub_date")


admin.site.register(TravelAdvisoryMessage, TravelAdvisoryMessageAdmin)
