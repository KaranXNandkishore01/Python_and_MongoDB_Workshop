from django.contrib import admin
from .models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cname', 'email', 'phone', 'cadd', 'unm', 'pw')
    list_filter = ('cname', 'email')
    search_fields = ('cname', 'email', 'phone', 'unm')
    ordering = ('cname',)
