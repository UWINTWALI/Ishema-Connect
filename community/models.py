from django.db import models
from accounts.models import UserProfile



# models.py
from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to user profile
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Optional image field
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when post was created

    def __str__(self):
        return f"{self.user_profile.user.username}'s Post"


class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_profile}"
