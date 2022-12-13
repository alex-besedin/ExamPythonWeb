from django.contrib import admin

from KetoGo.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name',)
    search_help_text = 'Search product by name...'
    ordering = ('category', 'name',)
