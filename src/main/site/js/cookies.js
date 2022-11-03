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

function setCookie(cookieName, cookieValue, expirationInDays) {
    const date = new Date();
    date.setTime(date.getTime() + (expirationInDays*24*60*60*1000));
    const cookieFormated = `${cookieName}=${cookieValue};expires=${date.toUTCString()};path=/`;
    document.cookie = cookieFormated;
}

function deleteCookie(cookieName) {
    const expires = "expires=Thu, 01 Jan 1970 00:00:00 UTC";
    document.cookie = `${cookieName}=; ${expires}; path=/;`;
}