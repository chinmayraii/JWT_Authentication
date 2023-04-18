from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import status


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            data = User.objects.all()
            serializer =RegisterSerializer(data,many = True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response( serializer.data,status=status.HTTP_400_BAD_REQUEST)    



