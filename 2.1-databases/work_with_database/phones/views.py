from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_name = request.GET.get("sort")
    if (sort_name == "min_price"):
        phones = Phone.objects.order_by("price")
    elif (sort_name == "max_price"):
        phones = Phone.objects.order_by("price").reverse()
    else:
        phones = Phone.objects.order_by(sort_name)
    context = {
        'phones':phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone':phone
    }
    return render(request, template, context)
