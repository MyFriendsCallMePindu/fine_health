# Register your models here.
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'service',
        'preferred_date',
        'status',
        'created_at'
    )
    list_filter = ('status', 'service')
    search_fields = ('full_name', 'phone')
    list_editable = ('status',)
