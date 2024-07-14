"""IMPORTS"""
# RESPONSE 
from django.http.response import HttpResponseBadRequest, JsonResponse

# AUTH
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# DECORATORS
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# PYTHON
import json
from decouple import config

"""VIEWS"""

# TOKEN GENERATION
@require_http_methods(["GET"])
def generate_token(request):

    # token 
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token}, safe=True)

# SESSIONS-LOGIN-ONLY-DOCTORS
@csrf_protect
@require_http_methods(["POST"])
def log_in(request):

    # json formatter
    data        = json.loads(request.body)

    # credentials
    user_name   = data.get("user_name")
    password    = data.get("password") 

    # authentication 
    user        = authenticate(username=user_name, password=password)
    if user is None:

        # wrong credentials(400)
        return HttpResponseBadRequest(content="Wrong Credentials") 
    
    # doctors group
    groups  = user.groups.all()  

    # no doctor's group
    group_names = [group.name for group in groups]
    if "Doctors" not in group_names:

        # wrong sesion data (400)
        return HttpResponseBadRequest(content="User doesn't belong to Doctors Group")

    #creation session
    login(request,user)
    return JsonResponse({"message":"Success"}, safe=True) 

# SIMPLE-LOGGIN-VALIDATION
@csrf_protect
@require_http_methods(["GET"])
def log_validation(request):
    
    if not request.user.is_authenticated:

        return HttpResponseBadRequest(content="No Authorization for this Website")

    return JsonResponse({"message":"Success"},safe=True)    

# SESSIONS-LOGOUT
@csrf_protect
@require_http_methods(["POST"])
@login_required
def log_out(request):

    # close sessions
    try:
        logout(request)

    except:
        
        # wrong sesion data (400)
        return HttpResponseBadRequest(content="Problems Handling Session, try later")
        
    # delete session data - 2x times
    request.session.flush()
    return JsonResponse({"message":"Success"},safe=True) 

# ROOT-USER FOR DEPLOY
@csrf_protect
@require_http_methods(["GET"])
def root_user(request):

    # csrf-protect
        # given by decorator
        # token
        # cookie

    # super-user exists
    superuser = User.objects.filter(username= config("superuser_name"))
    if superuser.exists() :

        return HttpResponseBadRequest(content="Wrong")

    # create superuser
    superuser = User.objects.create_superuser(
        username= config("superuser_name"), 
        email= config("superuser_email"), 
        password= config("superuser_password"),
    )
    superuser.save()

    return JsonResponse({"message":"Success"}, safe=True)