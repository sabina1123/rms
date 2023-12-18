from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    
    def update(self,category:Category,validated_data): #override the abstract method
        category.name=validated_data.get('name') #
        category.save()
        return category 
    

        
        
        