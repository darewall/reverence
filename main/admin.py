from django.contrib import admin
from .models import Size, Category, ClothingItem, ClothingItemSize


class ClothingItemStzeInline(admin.TabularInline):
    model = ClothingItemSize
    extra = 4


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'description', 'slug', 'category', 'created_at', 'updated_at', 'discount', 'price')
    list_filter = ('created_at', 'available', 'category')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    inlines = [ClothingItemStzeInline]








# Register your models here.
