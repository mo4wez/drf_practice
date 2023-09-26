from django.shortcuts import render

from .models import Product

def show_data(request):
    queryset = Product.objects.filter(id=4324)

    return render(request, 'store/detail.html')
