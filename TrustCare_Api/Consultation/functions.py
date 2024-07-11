"""IMPORTS"""
# PYTHON
from datetime import datetime

# LIBRARIES FOR REGEX , MATH
import math

# LIBRARIES FOR ROOTS
from pathlib import Path
from decouple import config

# LIBRARIES FOR PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# LIBRARIES FOR SENDING EMAILS
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders


"""FUNCTIONALITIES"""
# TODAY DATE
def current_date():

    date = datetime.today()

    return date

# AGE OF PATIENTS
def age(birthday):

    # Get today's date
    today = datetime.today()
    
    # Calculate the age
    age = today.year - birthday.year
    
    # Check if the birthday has not occurred yet this year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    
    return age

# REPORT ON PDF
def divide_long_text(text, x):

    long_text       = text
    len_text        = len(text)
    text_area       = A4[0] - (2*x)                              
    char_len        = 20/4                                     
    total_char_fea  = math.floor(text_area / char_len)      
    total_lines     = math.floor(len_text / total_char_fea)             
    lines           = []

    for i in range(0, total_lines+1):
            
        lines.append(long_text[total_char_fea*i:total_char_fea*(i+1)])
        
    return lines

def create_text_object(canvas,text, x, y, fontsize):

    canvas.setFontSize(fontsize)
    text_object     = canvas.beginText(x,y)
    lines           = divide_long_text(text,x)
        
    for line in lines:
        text_object.textLine(line)

    return text_object

def create_pdf(id,name,last_name,type_document,number_document,home_address,email_address,phone_code,phone_number,symptoms,observation,prescription,doctor_full_name,doctor_collegiate_code):

    try:

        # GENERAL VARIABLES
        BASE_DIR            = Path(__file__).resolve().parent.parent
        file_name           = f"report_{id}.pdf" # consultation id
        server_path         = str(BASE_DIR / "media" / "reports" / file_name)
        media_path          = f"media/reports/{file_name}"
        file_format         = "A4"
        file_title          = f"Report N°{id}" # consultation id
        file_restaurante    = "TrustCare"
        file_ruc            = f"RUC - 20933784625"
        message_one         = 'Your health, our priority! We offer personalized medical services with a compassionate approach, ensuring comprehensive care for you and your family. From routine check-ups to specialized treatments, TrustCare is here to support your wellness journey. Trust us with your care!'
        file_number         = f"Report - N°{id}" # consultation id
        section             = [
            'Patient',
            'Symptoms',
            'Observation',
            'Prescription',
        ]


        # PDF ::::::: VARIABLES FOR SIZE
        width, height = A4
        y       = 0
        y_middle= height // 2
        y_end   = round(height)
        x       = 0
        x_middle= width // 2
        x_end   = round(width)
        tab_one = 20
        tab_two = 30

        # PDF ::::::: CREATING
        pdf = canvas.Canvas(
            server_path,
            pagesize= file_format
        )


        # PDF'S TITLE
        pdf.setTitle(file_title)


        # CLINICS NAME + RUC
        pdf.setFontSize(20)
        pdf.drawString(tab_one,y_end-80,file_restaurante)
        pdf.setFontSize(15)
        pdf.drawString(tab_one,y_end-110,file_ruc)


        # MESSAGE 
        text = create_text_object(pdf,message_one,tab_one,y_end-143,11)
        pdf.drawText(text)


        # REPORT NUMBER
        pdf.rect(tab_one, y_end-230, x_middle-15,30)
        pdf.setFontSize(15)
        pdf.drawString(tab_two, y_end-222, file_number)


        # PATIENT 
        pdf.setFontSize(13)
        pdf.drawString(tab_one,y_middle+150,section[0])
        pdf.line(tab_one, y_middle+145, x_middle, y_middle+145)
        pdf.setFontSize(11)
        pdf.drawString(tab_two,y_middle+130,f'- Full Name : {name} {last_name}')
        pdf.drawString(tab_two,y_middle+115,f'- Document : {number_document} ({type_document})')
        pdf.drawString(tab_two,y_middle+100,f'- Home Adress : {home_address}')
        pdf.drawString(tab_two,y_middle+85,f'- Email Adress : {email_address}')
        pdf.drawString(tab_two,y_middle+70,f'- Cellphone : ({phone_code}) {phone_number}')


        # SYMPTOMS 
        pdf.setFontSize(13)
        pdf.drawString(tab_one,y_middle+30,section[1])
        pdf.line(tab_one, y_middle+25, x_middle, y_middle+25)
        pdf.setFontSize(11)            
        text = create_text_object(pdf,symptoms,tab_one,y_middle+10,11)
        pdf.drawText(text) 

        
        # OBSERVATION
        pdf.setFontSize(13)
        pdf.drawString(tab_one,y_middle-80,section[2])
        pdf.line(tab_one, y_middle-85, x_middle, y_middle-85)
        pdf.setFontSize(11)            
        text = create_text_object(pdf,observation,tab_one,y_middle-100,11)
        pdf.drawText(text) 


        # PRESCRIPTION
        pdf.setFontSize(13)
        pdf.drawString(tab_one,y_middle-210,section[3])
        pdf.line(tab_one, y_middle-215, x_middle, y_middle-215)
        pdf.setFontSize(11)            
        text = create_text_object(pdf,prescription,tab_one,y_middle-230,11)
        pdf.drawText(text) 


        # DOCTOR + DATE
        pdf.setFont("Times-Roman",11)
        pdf.drawString(tab_one,y+60,f'Dr. {doctor_full_name}')
        pdf.drawString(tab_one,y+45,f'Collegiate Code - {doctor_collegiate_code}')
        pdf.drawString(tab_one,y+30,str(current_date()))


        # SAVING PDF
        pdf.save()

        return media_path

    except:
     
        return False  

# SENDING EMAIL
def send_email_report(id,email_adress,full_name):
    
    try:

        # GENERAL VARIABLES
        BASE_DIR        = Path(__file__).resolve().parent.parent
        file_name       = f"report_{id}.pdf" # consultation id
        server_path     = str(BASE_DIR / "media" / "reports" / file_name)
        email_sender    = config("email_sender")
        email_password  = config("email_password")
        email_receiver  = email_adress
        subject         = "Health's Consultation Report"
        body            = f"Dear {full_name}, TrustCare is sending the report with all details for your last consultation in our stablishments"

        # Create the container email message.
        msg             = EmailMessage()
        msg['From']     = email_sender
        msg['To']       = email_receiver
        msg['Subject']  = subject
        msg.set_content(body)

        # Make the message multipart
        msg.add_alternative(body, subtype='html')

        # Attach the image file
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

