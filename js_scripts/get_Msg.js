token = localStorage.getItem("accesstoken")
const msgUrl = 'http://127.0.0.1:5000/v2/api/messages'
const usrUrl = 'http://127.0.0.1:5000/v2/api/users';
function fetchUsers(){

    fetch(usrUrl, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(response => {
        data = response.Users;
        data.forEach(function(item, index, array) {
            //console.log(item["user_name"]);
            var users = item["user_name"];
            var h = document.createElement("BUTTON")                // Create a <h1> element
            var t = document.createTextNode(users);     // Create a text node
            h.appendChild(t);
            document.body.appendChild(h);
            var q = document.getElementsByTagName("BUTTON");
            //console.log(h.innerText);
            var w = h.innerText;
            //console.log(w);
            //console.log(typeof(w));
            var i;
            for (i=0; i<=w.length; i++){
                //console.log(w)
            }
            
            let data1 = {
                chat_room_user_2: w
            };
            h.addEventListener('click', (w)=>{
                fetch(`http://127.0.0.1:5000/v2/api/chat_room`, {
                    method: 'POST',
                    mode: 'cors',
                    headers: {
                        'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify(data1)
                })
                //placed my .then
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

// end .then
            })
            //END OF EVENT LISTENER
            // document.getElementById("users-list").innerHTML += (users
            // +"<br>");
          });
    })  
    
}
    
fetchUsers()

function fetchAll(){

fetch(msgUrl, {
    method: 'GET',
    mode: 'cors',
    headers: {
        'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
    }
})
.then(res => res.json())
.then(response => {
    data = response.userName;
    data.forEach(function(item, index, array) {
        console.log(item["user_name"]);
        console.log(item["msg"]);
        var username = item["user_name"];
        var msgs = item["msg"];
        document.getElementById("messages-list").innerHTML += (username + ":" + msgs
                +"<br>");
        });
    });
    
}  
// fetchAll() 
// all the data is one li
// each should be its own li list element

// function fetchAllUsers(){
//     fetch(usrUrl, {
//         method: 'GET',
//         mode: 'cors',
//         headers: {
//             'Content-Type': 'application/json', 'Authorization': `Bearer ${token}`
//         }
//     })
//     .then(res => res.json())
//     .then(response => {
//         data = response.Users;
//         var i;
//         for (i = 0; i < data.length; i++) { 
//             specificUser = data[i];
//             user_id = specificUser.user_id;
//             user_name = specificUser.user_name;
//             email = specificUser.email;
//             password = specificUser.password
//             document.getElementsByTagName('li').innerHTML += (user_name
//                 +"<br>");
//             //putUsersList(username)
//         }
//     })  
    
// }  
// fetchAllUsers()

// // function putUsersList(user_name){
// //     let newUser = document.createTextNode(user_name);
// //     user_name.appendChild(newUser);
// // }

// // function addTextNode(text) {
// //     var newtext = document.createTextNode(text),
// //         p1 = document.getElementById("p1");
  
// //     p1.appendChild(newtext);
// //   }
// //   </script
// //   </head>
  
// //   <body>
// //     <button onclick="addTextNode('YES! ');">YES!</button>
// //     <button onclick="addTextNode('NO! ');">NO!</button>
// //     <button onclick="addTextNode('WE CAN! ');">WE CAN!</button>
  
// //     <hr />
  
// //     <p id="p1">First line of paragraph.</p>
// can it work if the names are not buttons. i think. try
// associatee messages to chat room
// rethink this logic
// the w in the braces of the arrow function. not needed?