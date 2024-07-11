from django.contrib import admin
from .models import Patient, Assistant

# PATIENT APP
class PatientPanel(admin.ModelAdmin):
    search_fields = ["number_document", "name", "last_name"]
    
admin.site.register(Patient, PatientPanel)
admin.site.register(Assistant)
