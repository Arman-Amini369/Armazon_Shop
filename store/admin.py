from django.contrib import admin
from .models import Category, Product, Comment, Cart

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("name", "category", "price")
    search_fields = ("name", "price", "category")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "quantities")
    list_filter = ("product", "quantities")
    search_fields = ("product", "quantities")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "body")
    list_search = ("user", "product", "body")
    search_fields = ("user", "product", "body")