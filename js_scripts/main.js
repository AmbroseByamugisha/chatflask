token = localStorage.getItem("accesstoken")
//const msgUrl = 'http://127.0.0.1:5000/v2/api/messages';

function signUp() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let email = document.getElementById('email').value;
    
    const url = 'http://127.0.0.1:5000/v2/api/signup';

    let data = {
        user_name: username,
        email: email,
        password: password
    }
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        alert(response.message);
        if (response.message=="you have created an account"){
        window.location.replace('login.html');
        }
    })
}
function logIn() {
    let user_name = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    const url = 'http://127.0.0.1:5000/v2/api/login';

    let data = {
        user_name: user_name,
        password: password
    }
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        localStorage.setItem("accesstoken",response.access_token);
        if (response.message=='user logged in Successfully'){    
            window.location.replace('session.html');;
        }    
        else{
            alert(response.message);
            if (response.message=='user does not exist, do you want to signup'){
                window.location.replace('signup.html');
            }
            else{
                window.location.reload()
            }
        }
    })
}

function sendMessage() {
    let msg = document.getElementById('message').value;
    
    const url = 'http://127.0.0.1:5000/v2/api/messages';

    let data = {
        msg: msg
    }
    fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        alert(response.message);
        if (response.message=="msg sent successfully"){
        window.location.replace('session.html');
        }
    })
}

      