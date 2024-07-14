"""IMPORTS"""
# RESPONSE 
from django.http.response import HttpResponseBadRequest, JsonResponse, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist

# DECORATORS
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# MODELS
from Patient.models import Patient
from .models import Consultation,Doctor
from django.db.models import Max

# PYTHON
import json

# FUNCTIONALITIES
from .functions import age, current_date, create_pdf, send_email_report

"""VIEWS"""

# PERSONAL DATA FOR PATIENT
@csrf_protect
@require_http_methods(["GET"])
@login_required
def patient_data(request, document):

    # call patient
    try:
        patient = Patient.objects.get(number_document = document)

    except ObjectDoesNotExist:

        return HttpResponseBadRequest(content="Patient's data Doesn't Exist")
    
    except :

        return HttpResponseServerError(content="Unexpected Error Happend")

    # filter the necessary data
    data = {
        "name": patient.name + " " + patient.last_name,
        "age": age(patient.birthday),
        "home":patient.home_address
    }

    # send data   
    return JsonResponse({"data":data}, safe=True)

# DOCTORS IN SESSION
@csrf_protect
@require_http_methods(["GET"])
@login_required
def doctor_data(request):

    # user in session
    user    = request.user  
    groups  = user.groups.all()  

    # no groups for user
    if not groups.exists() :

        # wrong sesion data (400)
        return HttpResponseBadRequest(content="No Groups Associated")

    # no doctor's group
    group_names = [group.name for group in groups]
    if "Doctors" not in group_names:

        # wrong sesion data (400)
        return HttpResponseBadRequest(content="User doesn't belong to Doctors Group")
    
    # call doctor
    try:
        doctor  = Doctor.objects.get(name=user.first_name, last_name=user.last_name, email_address=user.email, user_id=user.id)

    except ObjectDoesNotExist:

        return HttpResponseBadRequest(content="Doctor Doesn't Exist")
    
    except :

        return HttpResponseServerError(content="Unexpected Error Happend")
    
    # filter the necessary data
    data = {
        "name": f'{doctor.name} {doctor.last_name}',
        "college_id" : doctor.collegiate_code,
    }

    # send data   
    return JsonResponse({"data":data}, safe=True)

# ADD NEW CONSULTATION
@csrf_protect
@require_http_methods(["POST"])
@login_required
def new_consultation(request):

    # user in session
    user    = request.user  
    groups  = user.groups.all()  

    # no groups for user
    if not groups.exists() :

        # wrong sesion data (400)
        return HttpResponseBadRequest(content="No Groups Associated")

    # no doctor's group
    group_names = [group.name for group in groups]
    if "Doctors" not in group_names:

        # wrong sesion data (400)
        return HttpResponseBadRequest(content="User doesn't belong to Doctors Group")

    # json formatter
    data        = json.loads(request.body)

    # doctor's data from session
    try:

        doctor  = Doctor.objects.get(name=user.first_name, last_name=user.last_name, email_address=user.email)

    except ObjectDoesNotExist:

        return HttpResponseBadRequest(content="Doctor's Data Doesn't exist")

    except :

        return HttpResponseServerError(content="Unexpected Error Happend")
    
    # patient's data from request
    try:

        patient = Patient.objects.get(number_document=data.get("patient_id"))

    except ObjectDoesNotExist:

        return HttpResponseBadRequest(content="Patient's Data Doesn't exist")

    except :

        return HttpResponseServerError(content="Unexpected Error Happend")

    # id for consultation
    try:
        max_id = Consultation.objects.aggregate(max_id=Max('id'))['max_id']
        next_id = max_id + 1 if max_id is not None else 1

    except ObjectDoesNotExist:

        return HttpResponseBadRequest(content="Patient's Data Doesn't exist")

    except :

        return HttpResponseServerError(content="Unexpected Error Happend")

    # creating patient's report pdf
    # patient_pdf = create_pdf(
    #     id = next_id, 
    #     name= patient.name,
    #     last_name= patient.last_name, 
    #     type_document = patient.type_document,
    #     number_document = patient.number_document,
    #     home_address = patient.home_address,
    #     email_address = patient.email_address,
    #     phone_code = patient.phone_code,
    #     phone_number = patient.phone_number,
    #     symptoms = data.get("symptoms"),
    #     observation = data.get("observation"),
    #     prescription = data.get("prescription"),
    #     doctor_full_name= f'{doctor.name} {doctor.last_name}',
    #     doctor_collegiate_code= doctor.collegiate_code,
    # )

    # if patient_pdf == False:

    #     return HttpResponseBadRequest(content="Couldn't store New Consultation on DB")

    # creating new consultation
    new_register = Consultation(
        date = current_date(),
        symptoms = data.get("symptoms"),
        observation = data.get("observation"),
        prescription = data.get("prescription"),
        # report = patient_pdf, 
        patient_id = patient,
        doctor = doctor, 
    ) 
    new_register.save()

    # sending email
    send_email_report(next_id,patient.email_address,patient.name + " " + patient.last_name)

    return JsonResponse({"message":"Success"},safe=True)

# CALL HISTORY
@csrf_protect
@require_http_methods(["GET"])
@login_required
def patient_history(request, document):

    # call patient
    try:
        patient = Patient.objects.get(number_document = document)

    except ObjectDoesNotExist:

        return HttpResponseBadRequest(content="Object Doesn't Exist")
    
    except :

        return HttpResponseServerError(content="Unexpected Error Happend")  
    
    # get old consultations
    history_db = Consultation.objects.filter(patient_id=patient.id).order_by('-date')
    if not history_db.exists():

        return JsonResponse({"data":[]}, safe=True)

    # json format for consultations
    history_json = []
    for consultation in history_db:
        
        doctor = Doctor.objects.get(id=consultation.doctor.id)
        doctor = f'{doctor.name} {doctor.last_name} - COD.{doctor.collegiate_code}'

        register = {
            "id" : consultation.id,
            "date": consultation.date,
            "symptom": consultation.symptoms,
            "observation": consultation.observation,
            "prescription" : consultation.prescription,
            "doctor": doctor,
        }

        history_json.append(register)

    # send data  
    return JsonResponse({"data":history_json}, safe=True)

