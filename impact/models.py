from django.db import models
from events.models import Event
from accounts.models import UserProfile

class VolunteerHours(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    hours = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user_profile} - {self.hours} hours"
    class Meta:
        verbose_name_plural = "Volunteer Hours"
