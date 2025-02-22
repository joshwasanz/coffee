from django.db import models

# Create your models here.

class Like(models.Model):
    CONTENT_TYPES = [
        ('post','Post'),
        ('comment','Comment')
    ]

    user = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='likes')
    post = models.ForeignKey('posts.Post',null=True,blank=True,on_delete=models.CASCADE,related_name='likes')
    comment = models.ForeignKey('comments.Comment',null=True,blank=True,on_delete=models.CASCADE,related_name='likes')
    content_type = models.CharField(max_length=10,choices=CONTENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likes'
        unique_together = [['user','post'],['user','comment']]

        