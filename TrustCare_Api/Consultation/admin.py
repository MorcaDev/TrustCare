from django.contrib import admin
from .models import Consultation,Doctor,Speciality,DoctorSpeciality

# CONSULTATION
class ConsultationPanel(admin.ModelAdmin):
    search_fields = ["date"]
admin.site.register(Doctor)
admin.site.register(Speciality)
admin.site.register(DoctorSpeciality)
admin.site.register(Consultation, ConsultationPanel)