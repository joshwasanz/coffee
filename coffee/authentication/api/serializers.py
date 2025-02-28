from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "bio", "avatar", "website",
                  "github_profile", "twitter_profile", "created_at", "updated_at"]