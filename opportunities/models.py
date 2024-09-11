from django.db import models
from accounts.models import UserProfile

class Organization(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    volunteer_limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = [
        ('PEN', 'Pending'),
        ('APP', 'Approved'),
        ('REJ', 'Rejected'),
    ]
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile} applied to {self.opportunity}"
