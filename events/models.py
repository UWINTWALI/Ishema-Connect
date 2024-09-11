from django.db import models
from opportunities.models import Organization, Opportunity
from accounts.models import UserProfile

class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    volunteer_limit = models.IntegerField()
    registered_volunteers = models.ManyToManyField(UserProfile, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
