from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','street','phone','birth_date']


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['id','name','supplier','description']




@admin.register(sales_person)
class sales_personAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','street','city','phone','birth_date','date_hired']


@admin.register(sales_order)
class sales_orderAdmin(admin.ModelAdmin):
    list_display=['id','customer','sales_person','time_order_taken','purchase_order_number','credit_card_number','credit_card_expire_date','name_on_card']



@admin.register(item)
class itemAdmin(admin.ModelAdmin):
    list_display=['id','product','size','color','price']



# @admin.register(sales_item)
# class sales_itemAdmin(admin.ModelAdmin):
#     list_display=['id','item','sales_order','quantity','discount','taxable','sales_tax_rate']
