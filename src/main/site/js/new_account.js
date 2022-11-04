const baseURL = "http://127.0.0.1:8080";

function loginPage() {
    window.location.href = "login.html";
}

function createAccount() {
    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (email === "" || password === "" || password === "") return;

    const url = baseURL + "/user/create";
    const Http = new XMLHttpRequest();
    Http.open("POST", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send(JSON.stringify({
        "email": email,
        "username": username,
        "password": password
    }));

    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
                alert(json_resp.detail);
                return;
            }
            window.location.href = "index.html"
            alert('conta criada com sucesso');
        }
    }
}