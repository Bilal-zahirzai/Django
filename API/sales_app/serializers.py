from dataclasses import fields
from rest_framework import serializers
from .models import customer,sales_order,product,sales_item,sales_person,item,sales_item

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields=['id','first_name','last_name','email','street','phone','birth_date']

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['id','name','supplier','description']

class sales_personSerializer(serializers.ModelSerializer):
    class Meta:
        model=sales_person
        fields=['id','first_name','last_name','street','city','phone','birth_date','date_hired']


class itemSerializer(serializers.ModelSerializer):
    product= serializers.SlugRelatedField(queryset=product.objects.all(),slug_field='name')
    class Meta:
        model=item
        fields=['id','product','size','color','price']

class sales_itemSerializer(serializers.ModelSerializer):
    item= serializers.SlugRelatedField(queryset=item.objects.all(),slug_field='id')
    sales_order= serializers.SlugRelatedField(queryset=sales_order.objects.all(),slug_field='id')
    class Meta:
        model=sales_item
        fields=['id','item','sales_order','quantity','discount','taxable','sales_tax_rate']

class sales_orderSerializer(serializers.ModelSerializer):
    customer= serializers.SlugRelatedField(queryset=customer.objects.all(),slug_field='first_name')
    sales_person= serializers.SlugRelatedField(queryset=sales_person.objects.all(),slug_field='first_name')
    class Meta:
        model=sales_order
        fields=['id','customer','sales_person','time_order_taken','purchase_order_number','credit_card_number','credit_card_expire_date','name_on_card']
