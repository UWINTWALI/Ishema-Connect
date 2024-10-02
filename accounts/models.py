from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from opportunities.models import Organization

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
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default-profile.png', blank=True, null=True, storage=default_storage)
    role = models.CharField(max_length=12, choices=USER_ROLE_CHOICES)
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    """This will allow you to access the organizations a user follows like this: request.user.userprofile.followed_organizations"""
    @property
    def followed_organizations(self):
        return Organization.objects.filter(organizationfollow__user=self.user)



# Automatically create or update UserProfile when a User is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
