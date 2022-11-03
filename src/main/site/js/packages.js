const baseURL = "http://127.0.0.1:8080";
let packageID;

function searchPackage() {
    const idPacote = document.getElementById("idPacote").value;
    var infoPacote = document.getElementById("infoPacote");
    infoPacote.innerHTML = "";
    
    if (idPacote == "") {
        return;
    }
    
    const url = `${baseURL}/packages/${idPacote}`;
    const Http = new XMLHttpRequest();
    Http.open("GET", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send();

    Http.onreadystatechange = function(){
        if (Http.readyState === XMLHttpRequest.DONE) {
            const status = Http.status;
            if (status == 0 || (status >= 200 && status < 400)) {
                const result = JSON.parse(Http.responseText);
                if (result.status_code != undefined) {
                    infoPacote.innerHTML = 'Não encontramos um pacote com o ID informado.'
                    return;
                }

                infoPacote.innerHTML += `<strong> Start date: </strong> ${result.start_date} <br />`;
                infoPacote.innerHTML += `<strong> Stay time: </strong> ${result.stay_time} <br />`;
                infoPacote.innerHTML += `<strong> Destinations: </strong> ${result.destinations} <br />`;
                infoPacote.innerHTML += `<strong> Start destination: </strong> ${result.start_destination} <br />`;
                infoPacote.innerHTML += `<strong> Lowest price path: </strong> ${result.least_cost_path} <br />`;
                infoPacote.innerHTML += `<strong> package ID: </strong> ${result.package_id} <br />`;
                infoPacote.appendChild(createUpdatePackageButton());
                packageID = idPacote;
                
            } else {
                console.log(status);
            }
        }
    }
}

function createUpdatePackageButton() {
    const updatePackageButton = document.createElement("button");
    updatePackageButton.type = "button";
    updatePackageButton.onclick = updatePackage;
    updatePackageButton.innerHTML = "Pesquisar menor caminho";
    return updatePackageButton;
}

function updatePackage() {
    if (!packageID) return;

    const url = `${baseURL}/packages/update/${packageID}`;
    const Http = new XMLHttpRequest();
    Http.open("POST", url, true);
    Http.setRequestHeader("Accept", "application/json");
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send();

    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
                alert(json_resp.detail);
                return;
            }
            alert('Pacote atualizado');
        }
    }
}