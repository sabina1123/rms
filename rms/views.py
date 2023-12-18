from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView


# Create your views here.
"""class CategoryList():
    
    
    def get(self,request):
        category=Category.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'details':"Category has been Created",
            },
        status=status.HTTP_201_CREATED)
        
class CategoryDetail(APIView):
    def get(self,request,pk):

           category=get_object_or_404(Category,pk=pk)
           serializer=CategorySerializer(category)
           return Response(
              serializer.data
            )

        
        
    def delete(self,request,pk):
        try:
            category=Category.objects.get(pk=pk)
            order_items=OrderItems.objects.filter(food__category=category).count()
            if order_items>0:
                raise serializers.ValidationError({
                   'details':"You can't delete this category it has many order Items"
            })
            
            category.delete()
            return Response({
               'details':'Data has been deleted',
            },
            status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({
                'details':"Data no found",
            },
            status=status.HTTP_404_NOT_FOUND
            )
    
    
    def put(self,request,pk):
         category=get_object_or_404(Category,pk=pk)
         serializer=CategorySerializer(category,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         
         return Response({
              'details':'data has been updated',
         }
        )"""
        
class CategoryList(ListAPIView,CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
class CategoryDetail(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    
    def delete(self,request,pk):
        try:
            category=Category.objects.get(pk=pk)
            order_items=OrderItems.objects.filter(food__category=category).count()
            if order_items>0:
                raise serializers.ValidationError({
                   'details':"You can't delete this category it has many order Items"
            })
            
            category.delete()
            return Response({
               'details':'Data has been deleted',
            },
            status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({
                'details':"Data no found",
            },
            status=status.HTTP_404_NOT_FOUND
            )
          