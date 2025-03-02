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
            serializer.save(author=request.user,topics=request.data['topics'])
            print(request.data['topics'])

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_post(request,pk):

    post = Post.objects.get(id=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post,context={'request':request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if post.author != request.user:
            return Response({"detail":"Not authorized"},status=status.HTTP_403_FORBIDDEN)
        serializer = PostSerializer(post,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if post.author != request.user:
            return Response({"detail":"Not authorized"},status=status.HTTP_403_FORBIDDEN)
        
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

