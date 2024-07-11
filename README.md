# [Clinics System Based on Web ](https://git-scm.com/)  
![Banner](https://github.com/MorcaDev/TrustCare/blob/master/Demos/banner.png "TrustCare")

## Project Overview
----------
TrustCare Clinic System 🥼 , It's a web aplication in which doctors 👨‍⚕️ can idetify themselves and start the consultation process 🧬 , recording a new registration for the history of the patients on databases 📙, the history can also be accessed by doctor at the moment ⏰. This aplication has also a landing page where all people can see services pand basic information provided by TrustCare clinic👨‍👦  , and subscribe to a customized newsletter system 📥. Finally , the app uses a admin panel to allow the management of patients, doctors, assistants, posts involved in the core of the TrustCare Model Business 💹.

![LandingMobile](https://github.com/MorcaDev/TrustCare/blob/master/Demos/LandingPage_Mobile.gif "TrustCare")
![LandingDesktop](https://github.com/MorcaDev/TrustCare/blob/master/Demos/LandingPage_Desktop.gif "TrustCare")

## Flow of Aplication
----------
> **🌟 Landing Page** - for everyone to see services and information from TrustCare.
> **📫 Newsletter System** - for everyone to get enrolled in a chain of posts sent automatically using a panel admin.
> **🔐 Authenticacion Layers** - to validate recorded doctors data and get acess to the consultation system.
> **📝 Consultation System** - for doctors to register new consultations and check previous ones.
> **📂 Panel Admin** - for managing patients, doctors, authorization, groups, posts in newsletter.
> **📌 Important** - For more details about processes, authorizations look the documents processes and requirements.

![ConsultationSystem](https://github.com/MorcaDev/TrustCare/blob/master/Demos/ConsultationSystem_Mobile.gif "TrustCare")
![NewsletterSystem](https://github.com/MorcaDev/TrustCare/blob/master/Demos/NewsletterSystem.gif "TrustCare")

## Features
1. Client-Server architecture.
2. Independent server for Frontend and backend.
3. Landing page.
4. Integrated API.
5. Admin panel in API.
6. Cors policy.
7. Session Authentication.
8. CSRF token.
9. Automatic emails sending.
10. Relational DB.
11. Json conventions.
12. Responsive Design.

## Tech Stack
| Area | Technologies |
| ------ | ------ |
| Frontend | [Html](https://www.w3schools.com/html/), [Css](https://www.w3schools.com/css/), [Js](https://www.w3schools.com/js/), [Bootstrap-Studio](https://bootstrapstudio.io/), [Sweetalert](https://sweetalert.js.org/) |
| Backend | [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), [Django-Cors](https://pypi.org/project/django-cors-headers/), [Pytest-Django](https://pytest-django.readthedocs.io/en/latest/), [Reportlab](https://www.reportlab.com/), [Decouple](https://pypi.org/project/python-decouple/) |
| Database | [Sqlite3](https://www.sqlite.org/), [PostgreeSQL](https://www.postgresql.org/) |
| VCS  | [Git](https://git-scm.com/) |
| Server | [Linux](https://www.linux.org/)|
| Deployment |  ......, [Render](https://render.com/)  |

## Usage
The project TrustCare Clinics System, is designed with Client-Server arquitecture where aditionally the backend service (API) and frontend service (GUI) are hosted in different servers, but they interact to each other with secure layers.
> Backend: **https://render.....**
> Frontend: **https://githubpages.....**

## Installation
Instructions step by step for installing the project locally
**Full repo**
```sh
$git clone https://github.com/MorcaDev/TrustCare.git
 ```
**Backend Service**
 ```sh
$cd TrustCare-deploy/TrustCare_Api
$python -m venv venv
> Select virtual env
$pip install -r requirements.txt
> Create enviromental variables : email_sender , email_password 
$python manage.py makemigrations
$python manage.py migrate
$python manage.py runserver 
> Verify that the port is : 127.0.0.1:8000
 ```
**Frontend Service** 
 ```sh
$cd TrustCare-deploy/TrustCare_Front
> Live server Extension
> Verify that the port is : 127.0.0.1:3000
 ```

## Api
This API provides the logic behind the processes involved in a clinic system. 
-    **Authentication**
        - To get access for consultation system (only for doctors) and admin panel (for assistants and root user).
        - | Endpoint | Purpose | 
            | ------ | ------ | 
            | generate_token/ | To generate a csrfk token (not cookie) | 
            | log_in/ | To authenticate a user and create sessions for consultation system | 
            | log_validation/ | To enable or block interfaces provided by frontend server based on active sessions | 
            | log_out/ | To close sessions | 
            | admin/login/?next=/admin/ | To start a session in admin panel | 
            | admin/ | To use panel admin (handle tables) | 
            | admin/logout/ | To close sessions |
-    **Consultations**
        - To create new consultations and read patient's personal and medical history data. 
        - | Endpoint | Purpose |
            | ------ | ------ | 
            | patient_data/<str:document>/| To get patient's personal data |
            | doctor_data/| To get Doctort's personal data | 
            | new_consultation/ | To create a new consultation | 
            | patient_history/<str:document>/ | To get patient's history | 
-    **Newsletter System**
        - To assocciate new emails and automatic email sending.
        - | Endpoint | Purpose |
            | ------ | ------ |
            | new_email/ | To register new email in newsletter system  model |
            | drop_email/<str:email>/ | To drop an email using link sent by emails | 
            | admin/Newsletter/newsletteremail/<id:pk>/delete/ | To drop an email usin panel admin| 
            | admin/Newsletter/post/add/ | To create new emails and send it automatically | 

-    **Management of patients,assistants,doctors,groups**
        - To interact with all tables and groups.
        - | Table | Purpose |
            | ------ | ------ |
            | user | for creating new users  |
            | doctor | new doctors associated to a user |
            | assistant | new assistants associated to a user |
            | Groups |  to add a user permissions |


## Contributing
For the ones who want to increase features and the scope of the project.
1. Fork repository
2. New Branch ('NewFeature')
    ```sh
    $git checkout -b NewFeature
    ```
3. Commit your changes
    ```sh
    $git commit -m 'Add some feature'
    ```
4. Push to the branch
    ```sh
    $git push origin NewFeature
    ```
5. Create a Pull Request

## Testing
There are 4 apps in the project (Newsletter, Patient, Consultation, Authentication) 
Each app contains a directory with the unit testing files nested (tests/tests_name.py).
The tests evaluate units such as models, urls, and views.

```sh
> Example with "Newsletter" app
$pytest Newsletter\tests\tests_models.py -v
$pytest Newsletter\tests\tests_views.py -v
$pytest Newsletter\tests\tests_urls.py -v
```

## Deployment
Detailed instructions for deploying the project online 🌐.
> Backend services - [Render](https://docs.render.com/deploy-django) 
> Frontend service - [githubpages](https://pages.github.com/) 

## License 
> 👨‍💻* This project is free to be used and improved for everybody, **@morcadev *.

## Acknowledgment
> ⚔️ Special thanks for open source tools and services **@git @render @python**.