from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_title = 'RMS'
admin.site.site_header = 'RMS'
admin.site.index_title = 'RMS'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    list_per_page=10
    
    
    
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields=('name','price')
    list_display=('name','price','category',)
    list_filter=('category',)
    autocomplete_fields=('category',)
    list_per_page=10
    
    
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    search_fields=('number',)
    list_display=('number','is_occupied')
    list_filter=('is_occupied',)
    list_per_page=10
    
    
    def number(self,table:Table):
        return f"Table No {table.number}"
    
    
class OrderItemInline(admin.TabularInline):
    model=OrderItems
    autocomplete_fields=('food',)
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields=('user',)
    list_display=('user','status','payment_status','table',)
    list_filter=('status','table','payment_status','table__is_occupied')
    autocomplete_fields=('user',)
    list_per_page=10
    list_editable=('status','payment_status')
    inlines=(OrderItemInline,)
    
    
    
    
#@admin.register(OrderItems)
#class OrderitemsAdmin(admin.ModelAdmin):
    #search_fields=('Orderitems',)
    #list_display=('food','order','foodid',)
    #list_filter=('food','order') 
    
     
