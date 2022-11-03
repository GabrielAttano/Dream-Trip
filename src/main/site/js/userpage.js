const baseURL = "http://127.0.0.1:8080"

function logout() {
    deleteCookie("userID");
    deleteCookie("username");
    alert("Logged out");
    window.location.href="index.html";
}

function validate() {
    const userID = getCookie("userID");
    const username = getCookie("username");

    if (userID === "") {
        window.location.href = "index.html";
        alert("Você precisa estar logado para acessas esta página");
    }
    else
    {
        createUserpageInfo();
    }
}

function createUserpageInfo() {
    const username = getCookie("username");
    const usernameElement = document.getElementById("username");
    usernameElement.innerHTML=  username;

    
    getUser(getCookie("userID"));
}

function createUserInfoContainer(key, value) {
    const keyElement = document.createElement("h3");
    keyElement.innerHTML = key;
    const valueElement = document.createElement("span");
    valueElement.innerHTML = value;
    const userInfoContainer = document.createElement("div");
    userInfoContainer.appendChild(keyElement);
    userInfoContainer.appendChild(valueElement);
    return userInfoContainer;
}

function getUser(userID) {
    const url = `${baseURL}/user/${userID}`;
    const Http = new XMLHttpRequest();
    Http.open("GET", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send();

    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
                alert("Erro ao carregar info do usuário, usuário não encontrado");
                return;
            }
            const userInfoElement = document.getElementById("userInfo");
            for (let key in json_resp) {
                if (key === "id") {
                    continue;
                }
                const userInfoContainer = createUserInfoContainer(key, json_resp[key]);
                userInfoElement.appendChild(userInfoContainer);
            }
        }
    }
}

function deleteCookie(cookieName) {
    const expires = "expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = `${cookieName}=; ${expires}; path=/;`;
}

function getCookie(cookieName) {
    const cookies = document.cookie.split(";");
    if (cookies.length <= 1) return "";
    for (cookie of cookies) {
        let [cookieKey, cookieValue] = cookie.split("=");
        cookieKey = cookieKey.trim();
        cookieValue = cookieValue.trim();
        if (cookieKey === cookieName) return cookieValue;
    }
}

validate()