from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from.serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializers = UserSerializer(data=request.data)

    if serializers.is_valid():
        user = User(
            username = serializers.validated_data['username'],
            email=serializers.validated_data.get('email', ""),
        )
        user.set_password(serializers.validated_data['password'])
        user.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response(
            {"message":"User registration complete",
             "access_token":access_token,
             "refresh_token":str(refresh)},

            status=status.HTTP_201_CREATED)
    
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
