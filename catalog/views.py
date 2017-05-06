from django.shortcuts import render
from .models import Product, Category


def product_list(request):

    context = {
        'products': Product.objects.all()
    }

    return render(request, 'catalog/product_list.html', context)


def category(request, slug):

    Category_get = Category.objects.get(slug=slug)

    context = {
        'current_category': Category_get,
        'product_list': Product.objects.filter(category=Category_get),
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    context = {
        'product' : Product.objects.get(slug=slug)
    }
    return render(request, 'catalog/product.html', context)