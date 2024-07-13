// login validation
document.addEventListener("DOMContentLoaded",async function(event) {

    // fetch - token
    const tokenResponse = await fetch('https://trustcare.onrender.com/TrustCare/generate_token/', {
        method: 'GET',
        credentials: 'include', 
    });

    // token answer
    if (tokenResponse.ok) { 

        // JSON formatter
        const tokenData = await tokenResponse.json();
        const csrf_token = tokenData.csrf_token;

        // fetch - loginvalidation
        const logvalidationResponse = await fetch('https://trustcare.onrender.com/TrustCare/log_validation/', {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            },
        })

        // loginvalidation response
        if (logvalidationResponse.ok){

            // feedback message
            console.log("session active")

            // fetch - doctor
            const doctorResponse = await fetch('https://trustcare.onrender.com/TrustCare/doctor_data/', {
                method: 'GET',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
            });

            // doctor answer
            if (doctorResponse.ok) {

                // JSON formatter
                const doctorsJson = await doctorResponse.json();

                // reading doctor data
                const doctorsData = doctorsJson["data"]

                //  writing doctor data in html
                doctor_name.value = doctorsData["name"]
                doctor_code.value = doctorsData["college_id"]

            } else {

                // unexpected error
                swal("Error..!", "Something Wrong Happened, please try later", "error");
                console.error('Doctor failed:', doctorResponse.status);
                        
            }

        }else{

            // errorbased
            logvalidationResponse.text().then(errorText => {
              
                // sweet alert
                swal({
                    title: "No Permissions",
                    text: errorText,
                    icon: "error",
                    timer: 3000,
                    buttons: false,

                }).then((value) => {

                    // moving to system webpage for doctors
                    window.location.href = 'http://127.0.0.1:3000/'
                })
            });   
        }

    } else {

        // unexpected error
        swal("Error..!", "Something Wrong Happened, please try later", "error");
        console.error('Token request failed:', tokenResponse.status);
    }

});

// html component
const logout_button     = document.getElementById('logout_button');
const auto_fill         = document.getElementById('auto_fill');
const save              = document.getElementById('save') ;
const doctor_name       = document.getElementById('doctor_name');
const doctor_code       = document.getElementById('doctor_code');
const patien_name       = document.getElementById("patien_name");
const patient_age       = document.getElementById("patien_age");
const patien_home       = document.getElementById("patien_home");
const patient_id        = document.getElementById('patient_id')
const symptoms          = document.getElementById('symptoms')
const observations      = document.getElementById('observations')
const prescription      = document.getElementById('prescription')

// click event
logout_button.addEventListener('click', async function(event) {

    // script
    try {

        // fetch - token
        const tokenResponse = await fetch('https://trustcare.onrender.com/TrustCare/generate_token/', {
            method: 'GET',
            credentials: 'include',
        });

        // token response
        if (tokenResponse.ok) { 

            // JSON formatter
            const tokenData = await tokenResponse.json();
            const csrf_token = tokenData.csrf_token;

            // closing session
            const logoutResponse = await fetch('https://trustcare.onrender.com/TrustCare/log_out/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
            });

            // logout response
            if (logoutResponse.ok) {

                // feedback message
                swal({
                    title: "Succesfully Closed",
                    text: 'Window will be closed in 3 seconds',
                    icon: "info",
                    timer: 3000,
                    buttons: false,

                  }).then((value) => {

                    // moving to system webpage for doctors
                    window.location.href = 'http://127.0.0.1:3000/'
                  })


            } else {

                logoutResponse.text().then(errorText => {
                
                    // sweet alert
                    swal("Error..!", errorText, "error");
                    console.error('Logout failed:', logoutResponse.status);

                });
             
            }

        } else {

            // unexpected error
            swal("Error..!", "Something Wrong Happened, please try later", "error");
            console.error('Token request failed:', tokenResponse.status);
        }
        
    } catch (error) {
        console.error('Error:', error);
    }

});

// click event
auto_fill.addEventListener('click', async function(event) {

    const idValue = patient_id.value.trim(); 

    // Check if the patient value is empty
    if (idValue !== '') {

        try {

            // fetch - token
            const tokenResponse = await fetch('https://trustcare.onrender.com/TrustCare/generate_token/', {
                method: 'GET',
                credentials: 'include',
            });

            // token answer
            if (tokenResponse.ok) { 

                // JSON formatter
                const tokenData = await tokenResponse.json();
                const csrf_token = tokenData.csrf_token;

                // fetch - patient
                const patientResponse = await fetch('https://trustcare.onrender.com/TrustCare/patient_data/'+patient_id.value+ "/", {
                    method: 'GET',
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrf_token,
                    },
                });

                // patient response
                if (patientResponse.ok) {

                    // feedback message
                    const patientData = await patientResponse.json()
                    const patientDictionary = patientData["data"] 

                    // showing data
                    patien_name.value = patientDictionary["name"]
                    patient_age.value = patientDictionary["age"]
                    patien_home.value = patientDictionary["home"]

                    // invalidating changes in id
                    patient_id.disabled = true 

                } else {

                    patientResponse.text().then(errorText => {
                    
                        // sweet alert
                        swal("Error..!", errorText, "error");
                        console.error('Patients data does not exists', patientResponse.status);

                    });
                
                }

            } else {

                // unexpected error
                swal("Error..!", "Something Wrong Happened, please try later", "error");
                console.error('Token request failed:', tokenResponse.status);
            }
            
        } catch (error) {
            console.error('Error:', error);
        }

    } else {

        // empty input
        swal("Error..!", "Please, write an document for patient", "info");
    }

});

// click event
save.addEventListener('click', async function(event) {

    const patientidValue    = patient_id.value.trim(); 
    const patientidDisabled = patient_id.disabled; 
    const symptomsValue     = symptoms.value.trim(); 
    const observationsValue = observations.value.trim(); 
    const prescriptionValue = prescription.value.trim(); 

    // Check input
    if (patientidValue !== '' && patientidDisabled == true){

        if (symptomsValue !== '' && observationsValue !== '' && prescriptionValue !== ''){
            
            // script
            try {

                // fetch - token
                const tokenResponse = await fetch('https://trustcare.onrender.com/TrustCare/generate_token/', {
                    method: 'GET',
                    credentials: 'include',
                });

                // token answer
                if (tokenResponse.ok) { 

                    // JSON formatter
                    const tokenData = await tokenResponse.json();
                    const csrf_token = tokenData.csrf_token;

                    // fetch - consultation
                    const consultationResponse = await fetch('https://trustcare.onrender.com/TrustCare/new_consultation/', {
                        method: 'POST',
                        credentials: 'include',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrf_token,
                        },
                        body : JSON.stringify({
                            "patient_id"    : patientidValue,
                            "symptoms"      : symptomsValue,
                            "observation"   : observationsValue,
                            "prescription"  : prescriptionValue,
                        }),
                    });

                    // consultation answer
                    if (consultationResponse.ok) {

                        // feedback message
                        swal({
                            title: "Saved",
                            text: 'New consultation has been saved \n Reload in 3 seconds',
                            icon: "success",
                            timer: 3000,
                            buttons: false,

                          }).then((value) => {

                            // refreshing
                            window.location.href = 'http://127.0.0.1:3000/NewConsultation.html'
                          })

                    } else {

                        // error based
                        if (consultationResponse.status == 400) {

                            consultationResponse.text().then(errorText => {
                            
                                // sweet alert
                                swal("Error..!", errorText, "error");
                                console.error('Patients data does not exists', consultationResponse.status);
            
                            });

                        }else{
                            
                            // unexpected error
                            swal("Error..!", "Something Wrong Happened, please try later", "error");
                            console.error('Other failure:', consultationResponse.status);
                        }
                    
                    }

                } else {

                    // unexpected error
                    swal("Error..!", "Something Wrong Happened, please try later", "error");
                    console.error('Token request failed:', tokenResponse.status);
                }
                
            } catch (error) {
                console.error('Error:', error);
            }

        }else{
            
            // empty input
            swal("Error..!", "Please, write a complete consultation", "info");

        }

    }else{

        // empty input
        swal("Error..!", "Please, get information for patient", "info");
    }



});
