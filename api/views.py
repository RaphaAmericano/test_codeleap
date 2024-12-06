from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.serializers import PostSerializer
from base.models import Post
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def careers(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        # return Response(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({ 
                'username': serializer.data['username'],
                'title': serializer.data['title'],
                'content': serializer.data['content'],
                }, status=status.HTTP_201_CREATED)
        return JsonResponse({ 'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return JsonResponse({ 'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PATCH','DELETE'])
def careers_param_request(request, id):
    if request.method == 'PATCH':
        try: 
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'content': serializer.data['content'],
                    'title': serializer.data['title']
                }
                return JsonResponse(response_data, status=status.HTTP_200_OK)
            
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return JsonResponse({ 'error': 'Post not found' }, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        try: 
            post = Post.objects.get(id=id)
            post.delete()
            return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return JsonResponse({ 'error':'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        
    else:
        return JsonResponse({ 'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)