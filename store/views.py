from django.shortcuts import render
from django.db.models import Q

from .models import Product, OrderItem, Customer, Order

def show_data(request):
    queryset = Product.objects.filter(~Q(inventory__lt=30))
    print(list(queryset))

    return render(request, 'store/detail.html',)
