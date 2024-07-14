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
const logout_button     = document.getElementById('logout_button')
const logout_button_2   = document.getElementById('logout_button_2')

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
logout_button_2.addEventListener('click', async function(event) {

    // general erros
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

            // closing session
            const logoutResponse = await fetch('https://trustcare.onrender.com/TrustCare/log_out/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
            });

            // logout answer
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

                // error based
                if (logoutResponse.status == 400) {

                    logoutResponse.text().then(errorText => {
                    
                        // sweet alert
                        swal("Error..!", errorText, "error");
                        console.error('Logout failed:', logoutResponse.status);
    
                    });

                }else{
                    
                    // unexpected error
                    swal("Error..!", "Something Wrong Happened, please try later", "error");
                    console.error('Other failure:', logoutResponse.status);
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

});