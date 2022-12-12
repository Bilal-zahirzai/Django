from codecs import StreamWriter
import email
from types import CoroutineType
from unicodedata import name
from django.db import models

class customer(models.Model):
    first_name= models.CharField(max_length=30,blank= False )
    last_name=models.CharField(max_length=30,blank=False)
    email=models.CharField(max_length=50, blank=False)
    street =models.CharField(max_length=30, blank=False)
    phone =models.CharField(max_length=50)
    birth_date=models.DateField()

    def __str__(self):
        return self.first_name
    


class product(models.Model):
    name = models.CharField(max_length=30,blank= False )
    supplier = models.CharField(max_length=30,blank= False )
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class sales_person(models.Model):
    first_name= models.CharField(max_length=30,blank= False )
    last_name =models.CharField(max_length=30,blank= False )
    street =models.CharField(max_length=30,blank= False )
    city =models.CharField(max_length=30,blank= False )
    phone= models.IntegerField()
    birth_date=models.DateField()
    date_hired= models.DateField()
    def __str__(self):
        return self.first_name




class sales_order(models.Model):
    customer=models.ForeignKey(customer,related_name="customer",on_delete=models.CASCADE)
    sales_person=models.ForeignKey( sales_person ,related_name="sales_person",on_delete=models.CASCADE)
    time_order_taken=models.IntegerField()
    purchase_order_number=models.IntegerField()
    credit_card_number=models.IntegerField()
    credit_card_expire_date=models.DateField()
    name_on_card=models.CharField(max_length=40)
    def __str__(self):
        return self.name_on_card



class item(models.Model):
    product = models.ForeignKey(product,related_name="product",on_delete=models.CASCADE)
    size =models.IntegerField()
    color =models.CharField(max_length=20)
    price =models.IntegerField()
    




class sales_item(models.Model):
    item =models.ForeignKey(item, related_name="item",on_delete=models.CASCADE)
    sales_order=models.ForeignKey(sales_order,related_name="sales_order",on_delete=models.CASCADE)
    quantity=models.IntegerField()
    discount=models.IntegerField()
    taxable=models.IntegerField()
    sales_tax_rate=models.IntegerField()




