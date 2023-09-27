from django.shortcuts import render

from .models import Product, OrderItem, Customer, Order

def show_data(request):
    queryset_tom = Customer.objects.filter(first_name__icontains='tom')
    queryset = Order.objects.filter(customer__in=queryset_tom)

    print(list(queryset))

    return render(request, 'store/detail.html',)
