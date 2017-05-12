from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import ListView


class ProductListView(ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 3


class CategoryView(ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug= self.kwargs['slug'])
        return context


def product(request, slug):
    context = {
        'product': Product.objects.get(slug=slug)
    }
    return render(request, 'catalog/product.html', context)