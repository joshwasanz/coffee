from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField(max_length=500, blank=True)
    icon = models.ImageField(upload_to='topic_icons/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField('users.User',related_name='followed_topics')

    class Meta:
        db_table = 'topics'