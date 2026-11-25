from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'appointment_date', 'duration_minutes', 'status')
    list_filter = ('status', 'doctor')
    search_fields = ('reason', 'patient__last_name', 'doctor__last_name')
    readonly_fields = ('created_at', 'updated_at')
