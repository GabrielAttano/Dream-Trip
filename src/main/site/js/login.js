const baseURL = "http://127.0.0.1:8080";

function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    if (email === "" || password === "") return;
    
    const url = baseURL + "/user/auth";
    const Http = new XMLHttpRequest();
    Http.open("POST", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send(JSON.stringify({
        "email": email,
        "password": password
    }));

    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
                alert(json_resp.detail);
                return;
            }
            console.log("Autenticado com sucesso");
            setCookie("userID", json_resp.id, 1);
            setCookie("username", json_resp.username, 1);
            window.location.href = "index.html";
        }
    }
}

function logout() {
    deleteCookie("userID");
    deleteCookie("username");
}

function forgotPassword() {
    window.location.href = "forgot_password.html";
}

function createAccount() {
    window.location.href = "new_account.html";
}

function setCookie(cookieName, cookieValue, expirationInDays) {
    const date = new Date();
    date.setTime(date.getTime() + (expirationInDays*24*60*60*1000));
    const cookieFormated = `${cookieName}=${cookieValue};expires=${date.toUTCString()};path=/`;
    document.cookie = cookieFormated;
}

function getCookie(cookieName) {
    const cookies = document.cookie.split(";");
    for (cookie of cookies) {
        let [cookieKey, cookieValue] = cookie.split("=");
        cookieKey = cookieKey.trim();
        cookieValue = cookieValue.trim();
        if (cookieKey === cookieName) return cookieValue;
    }
}

function deleteCookie(cookieName) {
    const expires = "expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = `${cookieName}=; ${expires}; path=/;`;
}

