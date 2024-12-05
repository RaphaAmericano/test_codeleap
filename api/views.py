from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.serializers import PostSerializer
from base.models import Post

@api_view(['GET', 'POST'])
def careers(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
        print(serializer.error_messages)
        return Response(serializer.data)
    else:
        return Response('Method not allowed')

@api_view(['PATCH','DELETE'])
def careers_param_request(request, id):
    # ! adicionar ao patch validacao de dados para apenas editar conteudo e titulo
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
                return Response(response_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # serializer = PostSerializer(instance=post, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        # return Response(serializer.data)
        except Post.DoesNotExist:
            return Response('Post not found', status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try: 
            post = Post.objects.get(id=id)
            post.delete()
            return Response({ }, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response('Post not found', status=status.HTTP_404_NOT_FOUND)
        
    else:
        return Response('Method not allowed')