# from .models import Post
# from .serializers import PostSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
#
# # class PostList(generics.ListCreateAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer
# @api_view(['GET', 'POST'])
# def post_list(request):
#     """
#     List all Posts, or create a new Post.
#     """
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class PostDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer
# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk):
#     """
#     Retrieve, update or delete a Post.
#     """
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#