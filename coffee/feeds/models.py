from django.db import models

# Create your models here.

class UserFeedPrefernce(models.Model):
    user =  models.OneToOneField('users.User',on_delete=models.CASCADE,related_name='feed_preferences')
    preferred_topics = models.ManyToManyField('topics.Topic',related_name='preffered_by_users')
    exclude_topics = models.ManyToManyField('topics.Topic',related_name='exclude_by_users')
    feed_type = models.CharField(max_length=20,default='mixed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_feed_preferences'
        