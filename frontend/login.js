let form = document.getElementById('login-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("Form was submitted");

    let formdata = {
        'username': form.username.value,
        'password': form.password.value,
    };
    console.log(formdata);

    REQUEST_URL = 'http://127.0.0.1:8000/api/users/token';
    fetch(REQUEST_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formdata), 
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.access);
        if (data.access){
            localStorage.setItem('token',data.access)
            window.location= 'file:///Users/air/Downloads/Django-2021-master/frontend/projects-list.html'
        }
        else{
            alert("Username or password did not work")
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
