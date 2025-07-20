from django.shortcuts import render
from .models import SelectCar
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .serializer import SelectCarSerializer
from rest_framework import status


class SelectCarListView(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request = Request ):
        
        carchoice = SelectCar.objects.all()
        shop_serializer = SelectCarSerializer(carchoice, many = True)
        
        return Response(shop_serializer.data, status.HTTP_200_OK)
    
    def post(self, request = Request):
        
        serializer = SelectCarSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)
        
class SelectCarDetailApiView(APIView):
    
    def get(self, request = Request, request_id = int):
        
        car = SelectCar.objects.get(pk = request_id)
        
        if car in SelectCar:
            
            serializer = SelectCarSerializer(car)
            return Response(serializer.data, status.HTTP_200_OK)
        
        else:
            
            return Response(None, status.HTTP_404_NOT_FOUND)
         
        
        
