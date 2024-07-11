from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('generate_token/',generate_token, name="generate_token"),
    path('log_in/',log_in, name="log_in"),
    path('log_validation/',log_validation, name="log_validation"),
    path('log_out/',log_out, name="log_out"),
    path('root_user/',root_user, name="root_user"),
]