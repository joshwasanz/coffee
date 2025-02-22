from django.db import models

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        ordering = ['created_at']
        