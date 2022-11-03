const baseURL = "http://127.0.0.1:8080";

function forgotPassword() {
    const email = document.getElementById("email").value;

    const url = baseURL + "/user/forgot_password";
    const Http = new XMLHttpRequest();
    Http.open("POST", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send(JSON.stringify({
        "email": email,
    }));

    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
               alert(json_resp.detail);
                return;
            }
            console.log("Email enviado");
            window.location.href = "login.html"
            alert(`Email enviado para ${email}`);
        }
    }
}