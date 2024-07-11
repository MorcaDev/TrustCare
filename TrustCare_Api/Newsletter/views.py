"""IMPORTS"""
# RESPONSE 
from django.http.response import HttpResponse,HttpResponseBadRequest, JsonResponse, HttpResponseServerError

# DECORATORS
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# MODELS
from .models import Post, NewsLetterEmail

# PYTHON
import json

# FUNCTIONALITIES
from .functions import send_email_confirmation

"""VIEWS"""

# Create your views here.
@csrf_protect
@require_http_methods(["POST"])
def new_email(request):

    # catch json data
    data        = json.loads(request.body)

    # insertion in DB
    try:
        new_email = NewsLetterEmail(email = data.get("new_email"))
        new_email.save() 

    except:
        
        return HttpResponseBadRequest(content="Email Already Stored")

    # send email for confirmation
    send_email_confirmation(data.get("new_email"),"Welcome to TrustCare Newsletter..!!!", "You are enrolled in our newsletter system 😉📌✉️", True)

    return JsonResponse({"message":"Success"},safe=True)

@csrf_protect
@require_http_methods(["GET"])
def drop_email(request,email):

    # dropping in db
    try:

        # email from url
        specific_email = email

        # select email
        delete_email = NewsLetterEmail.objects.get(email=specific_email)

        # delete
        delete_email.delete()

    except:

        return HttpResponseBadRequest(content="Error Just Happended, Contact Trust Care")
    
    # send email for confirmation
    send_email_confirmation(email,"Unrolled to TrustCare Newsletter...", "It's sad to say it, but good bye, we hope see you soon 😓😓😓",False)

    return HttpResponse(f"<h1>Unrolling emails</h1><hr/><p>Your email '{specific_email}' has been dropped from our newsletter</p>")