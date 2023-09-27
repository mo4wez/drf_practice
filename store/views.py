from django.shortcuts import render

from .models import Product

def show_data(request):
    queryset = Product.objects.filter(
        name__icontains='car',
        datetime_created__year=2021,
        inventory__gt=50,
        )
    print(len(queryset))

    return render(request, 'store/detail.html', context={
        'products': list(queryset),
    })
