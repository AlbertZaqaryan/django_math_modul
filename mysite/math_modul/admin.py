from django.contrib import admin
from .models import Category, Modul
# Register your models here.

@admin.register(Category, Modul)
class CategoryModulAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']