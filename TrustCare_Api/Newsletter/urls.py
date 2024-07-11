from django.urls import path
from .views import *

urlpatterns = [
    path('new_email/',new_email, name="new_email"), # landing 
    path('drop_email/<str:email>/',drop_email, name="drop_email"), # from emails
]
