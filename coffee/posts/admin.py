from django.contrib import admin

from .models import Post

# Get all models dynamically and register them

admin.site.register(Post)