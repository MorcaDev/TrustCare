from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Post, NewsLetterEmail
from .functions import send_email_post,send_email_confirmation

# NEWSLETTER APP
class PostModel(admin.ModelAdmin):

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:        

        # no emails recorded
        list_emails = NewsLetterEmail.objects.all()
        if not list_emails.exists():

            # only save post
            super().save_model(request, obj, form, change)
        
        # emails recorded
        list_emails = list_emails
        list_reciever = []
        for email in list_emails:

            list_reciever.append(email.email)

        # saving new post   
        super().save_model(request, obj, form, change)

        # sending post to all recorded emails
        send_email_post(
            str(obj.title), 
            str(obj.content_text), 
            str(obj.content_media),
            list_reciever,
        )  

class NewsLetterEmailModel(admin.ModelAdmin):

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:        

        # saving new email  
        super().save_model(request, obj, form, change)

        # sending confirmation
        send_email_confirmation(
            str(obj.email),
            "Welcome to TrustCare Newsletter..!!!", 
            "You are enrolled in our newsletter system 😉📌✉️", 
            True
        )

    def delete_model(self, request: HttpRequest, obj: Any) -> None:

        # sending confirmation
        send_email_confirmation(
            str(obj.email),
            "Unrolled to TrustCare Newsletter...", 
            "It's sad to say it, but good bye, we hope see you soon 😓😓😓", 
            False
        )
        
        # deleting emails
        super().delete_model(request, obj)

admin.site.register(Post, PostModel)
admin.site.register(NewsLetterEmail, NewsLetterEmailModel)