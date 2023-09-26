from django.shortcuts import render

from .models import Product

def show_data(request):
    queryset = Product.objects.filter(category__title__icontains='student')
    print(len(queryset))

    return render(request, 'store/detail.html', context={
        'products': list(queryset),
    })
