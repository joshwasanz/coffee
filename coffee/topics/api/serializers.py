from rest_framework import serializers
from topics.models import Topic

class TopicSerializer(serializers.Serializer):
    class Meta:
        model = Topic
        fields = ["id", "name", "slug", "created_at"]