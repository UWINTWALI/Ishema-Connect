from django.db import models
from django.core.files.storage import default_storage
from django.contrib.auth.models import User




class Organization(models.Model):
    user_profile = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def follower_count(self):
        return 'dashboard.OrganizationFollow'.objects.filter(organization=self).count()



class Opportunity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    opportunity_picture = models.ImageField(upload_to='opportunity_pictures/',default='opportunity_pictures/', blank=True, null=True,storage=default_storage)
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
    user_profile = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE, related_name='applications')
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile} applied to {self.opportunity}"


class Donation(models.Model):
    PRIVACY_CHOICES = [
        ('share_name_amount', 'Share my name and amount'),
        ('share_name_hide_amount', 'Share my name but hide amount'),
        ('anonymous', 'Anonymous'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    privacy = models.CharField(max_length=30, choices=PRIVACY_CHOICES)
    donated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"Donation of {self.amount} with privacy {self.privacy}"
