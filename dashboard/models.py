from django.db import models
from django.contrib.auth.models import User
from opportunities.models import Organization

class OrganizationFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_organizations')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.username} follows {self.organization.name}"

