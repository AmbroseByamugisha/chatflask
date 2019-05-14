token = localStorage.getItem("accesstoken")
const chatUrl = 'http://127.0.0.1:5000/v2/api/chat_room';

function createChatRoom() {
    let chat_room_user_2 = document.getElementsByTagName("li");

    let data = {
        chat_room_user_2: chat_room_user_2
    }
    console.log(data);
    fetch(chatUrl, {
        method: 'POST',
        mode: 'cors',
        headers: {'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(response => {
        localStorage.setItem("accesstoken",response.access_token);
        if (response.message=='chat room added successfully'){    
            window.location.replace('chat_room.html');;
        }    
        else{
            alert(response.message);
            if (response.message=='chat does not exist, do you want to signup'){
                window.location.replace('session.html');
            }
            // else{
            //     window.location.reload()
            // }
        }
    })
}
// when we load the data store it somewhere where we can pick it