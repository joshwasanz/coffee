from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from posts.models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_list(request):

    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

        

