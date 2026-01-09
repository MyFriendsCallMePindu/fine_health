# Register your models here.
from django.contrib import admin
from .models import ServiceCategory, Service

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    inlines = [ServiceInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    list_filter = ('category',)
    list_editable = ('is_active',)
