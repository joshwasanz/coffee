from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser,Group,Permission


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # <-- Add unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # <-- Add unique related_name
        blank=True
    )
    
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    website = models.URLField(max_length=200, blank=True)
    github_profile = models.URLField(max_length=200, blank=True)
    twitter_profile = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name='following')

    class Meta:
        db_table = 'users'