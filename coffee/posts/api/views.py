from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from posts.models import Post
from .serializers import PostSerializer
from users.models import User

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def post_list(request):

    default_author = User.objects.get(username="joshwa")

    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user if request.user.is_authenticated else default_author,topics=request.data['topics'])
            print(request.data['topics'])

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        

