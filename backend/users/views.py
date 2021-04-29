# from .models import User, Athlete, Family
# from .serializers import UserSerializer, AthleteSerializer, FamilySerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# # class UserList(generics.ListCreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# @api_view(['GET', 'POST'])
# def user_list(request):
#     """
#     List all Users, or create a new User.
#     """
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class UserDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk):
#     """
#     Retrieve, update or delete a User.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
# # class AthleteList(generics.ListCreateAPIView):
# #     queryset = Athlete.objects.all()
# #     serializer_class = AthleteSerializer
# @api_view(['GET', 'POST'])
# def athlete_list(request):
#     """
#     List all Athletes, or create a new Athlete.
#     """
#     if request.method == 'GET':
#         athletes = Athlete.objects.all()
#         serializer = AthleteSerializer(athletes, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = AthleteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Athlete.objects.all()
# #     serializer_class = AthleteSerializer
# @api_view(['GET', 'PUT', 'DELETE'])
# def athlete_detail(request, pk):
#     """
#     Retrieve, update or delete a Athlete.
#     """
#     try:
#         athlete = Athlete.objects.get(pk=pk)
#     except Athlete.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = AthleteSerializer(athlete)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = AthleteSerializer(athlete, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         athlete.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # class FamilyList(generics.ListCreateAPIView):
# #     queryset = Family.objects.all()
# #     serializer_class = FamilySerializer
# @api_view(['GET', 'POST'])
# def family_list(request):
#     """
#     List all Families, or create a new Family.
#     """
#     if request.method == 'GET':
#         families = Family.objects.all()
#         serializer = FamilySerializer(families, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = FamilySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Family.objects.all()
# #     serializer_class = FamilySerializer
# @api_view(['GET', 'PUT', 'DELETE'])
# def family_detail(request, pk):
#     """
#     Retrieve, update or delete a Family.
#     """
#     try:
#         family = Family.objects.get(pk=pk)
#     except Family.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = FamilySerializer(family)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = FamilySerializer(family, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         family.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
