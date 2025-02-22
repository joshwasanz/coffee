from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id","username","email","bio","avatar","website",
        #           "github_profile","twitter_profile","followers_count",
        #           "following_count","is_following","created_at"]

        fields = "__all__"
        
        read_only_fields = ["email","created_at"]

