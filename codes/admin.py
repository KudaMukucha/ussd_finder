from django.contrib import admin
from . models import Category,Code

# Register your models here.
@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display =['name','slug','code','category','is_active']
    list_filter =['created','is_active','category','author']
    search_fields =['name','category']
    prepopulated_fields = {'slug':('name',)}
    ordering = ['is_active']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name']
    search_fields = ['name']