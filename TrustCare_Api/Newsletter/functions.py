# LIBRARIES FOR ROOTS
from pathlib import Path
from decouple import config

# LIBRARIES FOR SENDING EMAILS
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders

# SENDING EMAIL-CONFIRMATION-+/-
def send_email_confirmation(email_adress,subject,message,drop_email = True):
    
    try:

        # GENERAL VARIABLES
        email_sender    = config("email_sender")
        email_password  = config("email_password")
        email_receiver  = email_adress
        email_subject   = subject
        unfollow_link   = f"https://trustcare.onrender.com/TrustCare/drop_email/{email_adress}/"
        drop_message    = f"\n\nIf it's not you, please drop your association with the next link '{unfollow_link}'"
        body            = f"Dear {email_adress}, TrustCare is sending a message to confirm that {message} {drop_message if drop_email else ''}"

        # Create the container email message.
        msg             = EmailMessage()
        msg['From']     = email_sender
        msg['To']       = email_receiver
        msg['Subject']  = email_subject
        msg.set_content(body)

        # add SSL (layer of security)
        context = ssl.create_default_context()

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as s:
            s.login(email_sender,email_password)
            s.sendmail(email_sender,email_receiver,msg.as_string())

        
        return True

    except:

        return False

# SENDING EMAIL-POST
def send_email_post(title,content,media,email_adresses):
    
    try:

        # GENERAL VARIABLES
        BASE_DIR        = Path(__file__).resolve().parent.parent
        file_name       = media[6:]
        server_path     = str(BASE_DIR / "media" / media)
        email_sender    = config("email_sender")
        email_password  = config("email_password")
        email_receiver  = email_adresses
        subject         = title
        body            = content

        # Create the container email message.
        msg             = EmailMessage()
        msg['From']     = email_sender
        msg['To']       = email_receiver
        msg['Subject']  = subject
        msg.set_content(body)

        # Make the message multipart
        msg.add_alternative(body, subtype='html')

        # Attach the image file
        print(server_path)
        with open(server_path, 'rb') as attachment_file:
            file_data = attachment_file.read()

        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(file_data)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
        msg.attach(attachment)

        # add SSL (layer of security)
        context = ssl.create_default_context()

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as s:
            s.login(email_sender,email_password)
            s.sendmail(email_sender,email_receiver,msg.as_string())

        return True

    except:

        return False

