let totalTrechos = 0;
const maxTrechos = 4;
const minTrechos = 2;
const baseURL = "http://127.0.0.1:8080";

function createTrechosContainer() {

    const divOrigem = document.createElement('div');
    divOrigem.className = "ContainerOrigem";
    divOrigem.appendChild(createOrigemSelect());

    const divDestinos = document.createElement('div');
    divDestinos.className = "ContainerDestinos";
    for (; totalTrechos < minTrechos; totalTrechos++) {
        divDestinos.appendChild(createDestinoSelect());
    }

    document.getElementById("destinosSelector").appendChild(divOrigem);
    document.getElementById("destinosSelector").appendChild(divDestinos);
}

function newTrecho() {
    if (totalTrechos > maxTrechos) return;

    const containerDestinos = document.getElementsByClassName("ContainerDestinos")[0];
    containerDestinos.appendChild(createDestinoSelect());
    totalTrechos++;
}

function removeTrecho () {
    if (totalTrechos <= minTrechos) return;

    const divDestino = document.getElementById(`Destino${Number(totalTrechos) - 1}`);
    divDestino.remove();
    totalTrechos--;
}

function createOrigemSelect() {
    const origemSelect = createSelect("Origem");
    origemSelect.name = "destinos";
    origemSelect.id = "Origem";
    return origemSelect;
}

function createDestinoSelect() {
    const destinoSelect = createSelect("Destino");
    destinoSelect.name = "destinos";
    destinoSelect.id = `Destino${totalTrechos}`;
    return destinoSelect;
}

function createSelect(placeholderName) {
    const decolarDestinations = [
        [placeholderName, 'none'],
        ["Brasília", "BSB"],
        ["Rio Branco", "RBR"],
        ["Maceió", "MCZ"],
        ["Manaus", "MAO"],
        ["Salvador", "SSA"],
        ["Fortaleza", "FOR"],
        ["Vitória", "VIX"],
        ["Goiânia", "GYN"],
    ];
    
    const select = document.createElement("select");
    for (let i = 0; i < decolarDestinations.length; i++) {
        const option = document.createElement("option");
        option.value = decolarDestinations[i][1];
        option.innerHTML = decolarDestinations[i][0];
        select.add(option);
    }
    
    return select;
}

function createPackage() {
    if (!isValidPackage()) return;
    destinos = getDestinos();
    const origem = document.getElementById("Origem").value;
    const userID = getCookie("userID");
    const start_date = document.getElementById("start-date").value;
    const stay_time = document.getElementById("stay-time").value;
    if (!userID) {
        return alert("Você deve estar logado para criar um pacote");
    }

    const url = baseURL + "/packages/create";
    const Http = new XMLHttpRequest();
    Http.open("POST", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send(JSON.stringify({
        "start_date": start_date,
        "stay_time": stay_time,
        "destinations": destinos,
        "start_destination": origem,
        "user_id": userID
    }));
    
    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
                alert(json_resp);
                return;
            }
            alert(`Pacote criado com ID: ${json_resp.package_id}`);
            window.location.href = "index.html"
        }
    }
}

function isValidPackage() {
    const origem = document.getElementById("Origem").value;
    if (origem == "none") {
        alert("Deve selecionar origem");
        return false;
    }

    const destinos = getDestinos();

    for (let i = 0; i < destinos.length; i++) {

        const element = destinos[i];

        if (element == "none") {
            alert("Todos os destinos devem estar preenchidos");
            return false;
        }
        if (element == origem) {
            alert("Destino não pode se repetir com origem")
            return false;
        }

        for (let j = i+1; j < destinos.length; j++) {
            if (element == destinos[j]) {
                alert("Destinos não podem se repetir");
                return false;
            }
        }
    }

    return true;
}

function getDestinos() {
    const destinos = []
    for (let i = 0; i < totalTrechos; i++) {
        destinos.push(document.getElementById(`Destino${i}`).value);
    }
    return destinos;
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

createTrechosContainer();