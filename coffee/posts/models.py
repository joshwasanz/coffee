from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='post_covers/',null=True,blank=True)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE,related_name='posts')
    topics = models.ManyToManyField('topics.Topic',related_name='posts')
    published_at = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title}"