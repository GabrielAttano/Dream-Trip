const links = document.getElementsByClassName("links")[0];

function handleAuth() {
    
    const userID = getCookie("userID");
    const username = getCookie("username");
    let container = userID === "" ? createLoginContainer() : createUserContainer(username);
    links.appendChild(container);
}

function createLoginContainer() {
    const loginContainer = document.createElement("li");
    const loginElement = document.createElement("a");
    loginElement.href = "login.html";
    loginElement.innerHTML = "Login";
    loginContainer.appendChild(loginElement);
    return loginContainer;
}

function createUserContainer(username) {
    const userContainer = document.createElement("li");
    const userElement = document.createElement("a");
    userElement.href = "search_package.html";
    userElement.innerHTML = username;
    userContainer.appendChild(userElement);
    return userContainer;

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

handleAuth();