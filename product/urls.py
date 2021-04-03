from django.urls import path
from .views import products_list, product_add, product_delete, product_update

urlpatterns = [
    path('list/', products_list, name="product_list"),
    path('add/', product_add, name="product_add"),
    path('update/<int:id>/', product_update, name="product_update"),
    path('delete/<int:id>/', product_delete, name="product_delete"),
]
