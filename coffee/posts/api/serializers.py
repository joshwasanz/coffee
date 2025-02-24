from rest_framework import serializers
from posts.models import Post  # Import your Post model

from users.api.serializers import UserSerializer
from topics.api.serializers import TopicSerializer

class PostSerializer(serializers.ModelSerializer):
    
    author = UserSerializer(read_only=True)
    topics = TopicSerializer(many=True,read_only=True)
    

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "content", "cover_image",
                  "author", "topics", "published_at", "created_at", "updated_at",
                  ]
        read_only_fileds = ['author','created_at','updated_at']
