function login() {
    
}

function forgotPassword() {

}

function createAccount() {
    console.log(document.cookie);
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

setCookie("userID", "4002-8922", 1);
setCookie("username", "Gabriel Sá", 1);
console.log(getCookie("username"));