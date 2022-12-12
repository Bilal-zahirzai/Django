from django.urls import path
from .views import customerDetail,customerList,productDetail,productList,sales_itemDetail,sales_itemList,sales_orderDetail,sales_orderList,itemDetail,itemList,sales_personDetail,sales_personList
urlpatterns=[
    path('customer/',customerList.as_view()),
    path('customer/<int:pk>',customerDetail.as_view()),

    path('product/',productList.as_view()),
    path('product/<int:pk>',productDetail.as_view()),

    path('sales_person/',sales_personList.as_view()),
    path('sales_person/<int:pk>',sales_personDetail.as_view()),

    path('item/',itemList.as_view()),
    path('item/<int:pk>',itemDetail.as_view()),

    path('sales_item/',sales_itemList.as_view()),
    path('sales_item/<int:pk>',sales_itemDetail.as_view()),

    path('sales_order/',sales_orderList.as_view()),
    path('sales_order/<int:pk>',sales_orderDetail.as_view()),


]