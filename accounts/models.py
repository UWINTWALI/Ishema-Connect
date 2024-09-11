from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.storage import default_storage

"""UserProfile model extends the default Django User model"""
class UserProfile(models.Model):
    USER_ROLE_CHOICES = (
        ('volunteer', 'Volunteer'),
        ('organization', 'Organization'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    interests = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, storage=default_storage)
    role = models.CharField(max_length=12, choices=USER_ROLE_CHOICES)

    def __str__(self):
        return self.user.username

# Automatically create or update UserProfile when a User is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
