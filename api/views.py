
from .serializers import MyTokenObtainPairSerializer, UserSerializer, BlogSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status
from django.http import Http404




class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(APIView):
    
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class GetAllBlog(APIView):


    def get(self, request, format=None):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)


class CreateBlog(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        request.data["user"] = request.user.id
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteBlog(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.user == request.user:
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        else:
            return Response({"message":"you are not Authorized"})

    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.user == request.user:
            request.data["user"] = request.user.id
            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"you are not Authorized"})

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.user == request.user:
            blog.delete()
            return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"you are not Authorized"})