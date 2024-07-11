from django.urls import path
from .views import *

urlpatterns = [
    path('patient_data/<str:document>/',patient_data, name="patient_data"),
    path('doctor_data/',doctor_data, name="doctor_data"),
    path('new_consultation/',new_consultation, name="new_consultation"),
    path('patient_history/<str:document>/',patient_history, name="patient_history"),
]
