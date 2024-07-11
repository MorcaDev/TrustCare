// html component
const form = document.getElementById("form")

// submit event
form.addEventListener('submit', async function(event) {

    // Prevent default form submission
    event.preventDefault(); 

    // general erros
    try {

        // fetch - token
        const tokenResponse = await fetch('http://127.0.0.1:8000/TrustCare/generate_token/', {
            method: 'GET',
            credentials: 'include', 
        });

        // token response
        if (tokenResponse.ok) { 

            // JSON formatter
            const tokenData = await tokenResponse.json();
            const csrf_token = tokenData.csrf_token;

            // fetch - email
            const emailResponse = await fetch('http://127.0.0.1:8000/TrustCare/new_email/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
                body: JSON.stringify({
                    new_email: document.getElementById("email").value,
                }),
            });

            // login response
            if (emailResponse.ok) {

                // sweet alert
                swal("Success..!", "Email registered on Newsletter", "success");


            } else {

                // wrong credential message
                emailResponse.text().then(errorText => {
                    
                    // sweet alert
                    swal("Error..!", errorText, "error");
                    console.error('Email failed:', emailResponse.status);

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