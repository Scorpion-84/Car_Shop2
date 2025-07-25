from django.shortcuts import render
from .models import SelectCar
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .serializer import SelectCarSerializer
from rest_framework import status
from rest_framework import generics


class SelectCarListView(generics.ListCreateAPIView):
    
    #permission_classes = (IsAuthenticated)
    
    queryset = SelectCar.objects.all()
    serializer_class = SelectCarSerializer
        
class SelectCarDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = SelectCar.objects.all()
    serializer_class = SelectCarSerializer
            
         
        
        
