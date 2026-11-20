from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor, Patient, Specialty, User

admin.site.register(User, UserAdmin)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'license_number', 'phone')
    search_fields = ('last_name', 'first_name', 'license_number')
    filter_horizontal = ('specialties',)

    def get_readonly_fields(self, request, obj=None):
        # license_number est un identifiant métier : non modifiable après création
        if obj:
            return ('license_number',)
        return ()


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'national_id', 'phone', 'birth_date')
    search_fields = ('last_name', 'first_name', 'national_id')

    def get_readonly_fields(self, request, obj=None):
        # national_id est un identifiant métier : non modifiable après création
        if obj:
            return ('national_id',)
        return ()
