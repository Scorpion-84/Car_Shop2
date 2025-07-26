from django.shortcuts import render
from .models import SelectCar
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .serializer import SelectCarSerializer
from rest_framework import generics,status
from .serializer import SignUpSerializer


class SelectCarListView(generics.ListCreateAPIView):
    
    #permission_classes = (IsAuthenticated)
    
    queryset = SelectCar.objects.all()
    serializer_class = SelectCarSerializer
        
class SelectCarDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = SelectCar.objects.all()
    serializer_class = SelectCarSerializer
    
    
class SignUpView(generics.CreateAPIView):
    
    serializer_class = SignUpSerializer
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        
        return Response({
            'user': {
                'username': user.username, 
                'email': user.email}, 
            'message': 'User created successfully'
            },
                    status = status.HTTP_201_CREATED)
            
         
        
        
