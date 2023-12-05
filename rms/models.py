from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    

    def __str__(self):
        return self.name


class Food(models.Model):

    name=models.CharField(max_length=255)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Table(models.Model):

    number=models.IntegerField()
    is_occupied=models.BooleanField(default=False)

    def __str__(self):
        return f"Table no {self.number}"
    
class Order(models.Model):
    COMPLETED_CHOICE='C'
    PENDING_CHOICE='P'
    
    ORDER_STATUS_CHOICES=[
        (COMPLETED_CHOICE,'COMPLETED'),
        (PENDING_CHOICE,'PENDING'),
    ]

    
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.IntegerField()
    status=models.CharField(max_length=1,choices=ORDER_STATUS_CHOICES,default='PENDING_CHOICE')
    payment_status=models.BooleanField(default=False)


    def __str__(self):
        return self.name



class OrderItems(models.Model):

    food=models.ForeignKey(Food,on_delete=models.PROTECT)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
  



