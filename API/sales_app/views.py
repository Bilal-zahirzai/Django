from django.shortcuts import render
from .models import customer,sales_item,sales_order,sales_person,item,product
from .serializers import customerSerializer,sales_itemSerializer,sales_orderSerializer,sales_personSerializer,itemSerializer,productSerializer
from rest_framework import generics

class customerList(generics.ListCreateAPIView):
    queryset=customer.objects.all()
    serializer_class=customerSerializer

class customerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=customer.objects.all()
    serializer_class=customerSerializer



class productList(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=productSerializer

class productDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=product.objects.all()
    serializer_class=productSerializer


class sales_personList(generics.ListCreateAPIView):
    queryset=sales_person.objects.all()
    serializer_class=sales_personSerializer

class sales_personDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=sales_person.objects.all()
    serializer_class=sales_personSerializer


class sales_orderList(generics.ListCreateAPIView):
    queryset=sales_order.objects.all()
    serializer_class=sales_orderSerializer

class sales_orderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=sales_order.objects.all()
    serializer_class=sales_orderSerializer


class itemList(generics.ListCreateAPIView):
    queryset=item.objects.all()
    serializer_class=itemSerializer

class itemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=item.objects.all()
    serializer_class=itemSerializer


class sales_itemList(generics.ListCreateAPIView):
    queryset=sales_item.objects.all()
    serializer_class=sales_itemSerializer

class sales_itemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=sales_item.objects.all()
    serializer_class=sales_itemSerializer