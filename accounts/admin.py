from django.contrib import admin
from .models import CustomerAccount

@admin.register(CustomerAccount)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username",)
    list_filter = ("username",)
    search_fields = ("username",)