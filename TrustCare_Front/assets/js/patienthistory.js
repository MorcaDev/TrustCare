// login validation
document.addEventListener("DOMContentLoaded", async (event)=>{
  
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
        });

        // loginvalidation response
        if (logvalidationResponse.ok) {

            // feedback message
            console.log("session active")

        } else {

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
                    window.location.href = 'https://morcadev.github.io/TrustCare/'
                })

            });
            
        }

    } else {

        // unexpected error
        swal("Error..!", "Something Wrong Happened, please try later", "error");
        console.error('Token request failed:', tokenResponse.status);
    }
        
})

// html component
const logout_button     = document.getElementById('logout_button');
const auto_fill         = document.getElementById('auto_fill');
const patien_name       = document.getElementById("patien_name");
const patient_age       = document.getElementById("patien_age");
const patien_home       = document.getElementById("patien_home");
const patient_id        = document.getElementById('patient_id')
const acordion          = document.getElementById('accordion-1');

// click event
logout_button.addEventListener('click', async function(event) {

    // general erros
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
                    window.location.href = 'https://morcadev.github.io/TrustCare/'
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

    const patientidValue    = patient_id.value.trim(); 
    const patientidDisabled = patient_id.disabled; 

    // Check input
    if (patientidValue !== '' || patientidDisabled == true){

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
    
                    // fetch - history
                    const historyResponse = await fetch('https://trustcare.onrender.com/TrustCare/patient_history/'+patient_id.value+ "/", {
                        method: 'GET',
                        credentials: 'include',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrf_token,
                        },
                    });
    
                    // history message
                    const historyData = await historyResponse.json()
                    const historyList = historyData["data"] 
    
                    if (historyList.length !== 0){
    
                        acordion.innerHTML = ""

                        historyList.forEach(consultation => {
    
                            // creating html component
                            const acordion_div     = document.createElement("div")
                            acordion_div.id        = consultation["id"]
                            acordion_div.className = "accordion-item"
                            acordion_div.innerHTML = `
                                    <h2 class="accordion-header" role="tab">
                                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#accordion-1 .item-${consultation["id"]}" aria-expanded="false" aria-controls="accordion-1 .item-${consultation["id"]}" style="background: rgba(207,226,255,0);">${consultation["date"]}</button>
                                    </h2>
        
                                    <div class="accordion-collapse collapse item-${consultation["id"]}" role="tabpanel" data-bs-parent="#accordion-1" style="padding: 0px;width: 90%;margin: 0px auto;margin-bottom: 20px;border: 1px none rgba(124,143,198,0.77) ;border-top: 0px solid #19344f6c ;">
        
                                        <div class="accordion-body">
                                            <h3 style="font-size: 20px;">Symptoms</h3>
                                            <p class="mb-0">${consultation["symptom"]}</p>
                                            <h3 style="font-size: 20px;margin-top: 20px;">Observation</h3>
                                            <p class="mb-0">${consultation["observation"]}</p>
                                            <h3 style="font-size: 20px;margin-top: 20px;">Prescription</h3>
                                            <p class="mb-0">${consultation["prescription"]}</p>
                                            <h3 style="font-size: 20px;margin-top: 20px;">Doctor</h3>
                                            <p class="mb-0">${consultation["doctor"]}</p>
                                        </div>
        
                                    </div>
                            `
    
                            // adding component
                            acordion.appendChild(acordion_div)
                            
    
                        });
    
                    }else{
                        
                        acordion.innerHTML = "No Consultations recorded"
    
                    }
    
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

    }else{

        // empty input
        console.log('Patient ID is empty.');
        swal("Error..!", "Please, get information for patient", "info");
    }


});
