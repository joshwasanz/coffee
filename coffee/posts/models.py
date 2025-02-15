from django.db import models

# Create your models here.

class Post(models.Model):
    # author = connect to user model
    title = models.CharField(max_length=255)
    # picture = optional 
    caption_main = models.TextField()
    description = models.TextField() #optional
    # hashtags = optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    # comments = connect from comments model

    def __str__(self):
        return self.title