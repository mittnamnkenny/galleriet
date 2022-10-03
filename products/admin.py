from django.contrib import admin
from .models import Product, Category, Artist

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'category',
        'medium',
        'price',
        'added_on',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'nationality',
        'email',
        'phone_number',
        'added_on',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artist, ArtistAdmin)
