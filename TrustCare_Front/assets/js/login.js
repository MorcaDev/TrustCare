// html component
const form = document.getElementById('LoginForm')

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

            // fetch - session
            const loginResponse = await fetch('http://127.0.0.1:8000/TrustCare/log_in/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
                body: JSON.stringify({
                    user_name: document.getElementById('user_name').value,
                    password:  document.getElementById('password').value,
                }),
            });

            // login response
            if (loginResponse.ok) {

                // moving to system webpage for doctors
                window.location.href = 'http://127.0.0.1:3000/SystemHome.html'

            } else {

                // wrong credential message
                loginResponse.text().then(errorText => {
                    
                    // sweet alert
                    swal("Error..!", errorText, "error");
                    console.error('Login failed:', loginResponse.status);

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