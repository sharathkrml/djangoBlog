from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from blog.models import Post
from .serializers import PostSerializer

@api_view(['GET','POST'])
def posts_list(request):
        try:
            posts = Post.objects.all()
        except Post.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = PostSerializer(posts,many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def post_detail(request,id):
        try:
            posts = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = PostSerializer(posts)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PostSerializer(posts, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            posts.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)