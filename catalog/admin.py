from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug']


admin.site.register(Product, ProductAdmin)
