from django.shortcuts import render
from django.db.models import Q, F

from .models import Product, OrderItem, Customer, Order

def show_data(request):
    queryset = OrderItem.objects.filter(product_id=F('quantity'))
    print(list(queryset))

    return render(request, 'store/detail.html',)
