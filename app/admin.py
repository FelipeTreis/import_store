from django.contrib import admin

from app.models import Brand, Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('is_actived', 'name', )
    list_display_links = ('name', )
    list_editable = ('is_actived', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('is_actived', 'name', )
    list_display_links = ('name', )
    list_editable = ('is_actived', )
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('is_published', 'name', 'category', 'brand', 'value', 'state', )
    list_display_links = ('name', )
    list_editable = ('is_published', )
    list_filter = ('name', 'category', 'brand', 'value', 'state', )
    list_per_page = 10
    autocomplete_fields = ('brand', 'category', )
    search_fields = ('name', 'category', 'brand', 'value', 'state', )
    prepopulated_fields = {"slug": ('name', )}
