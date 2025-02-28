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


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)  
    

    user = authenticate(username=username,password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({
        "message": "Login successful",
        "access_token": access_token,
        "refresh_token": str(refresh)
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()  # Blacklist the refresh token
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
