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
                infoPacote.innerHTML += `<strong> Start destination: </strong> ${result.start_destination} <br />`;
                infoPacote.innerHTML += `<strong> Destinations: </strong> ${result.destinations} <br />`;
                infoPacote.innerHTML += `<strong> package ID: </strong> ${result.package_id} <br />`;
                if(result.least_cost_path != ""){
                    infoPacote.appendChild(createTripTable(result.least_cost_path,result.least_cost_path.length));
                }else{
                    infoPacote.appendChild(createUpdatePackageButton());
                }
                packageID = idPacote;
                
            } else {
                console.log(status);
            }
        }
    }
}

function createTripTable(path , tamanho){
    let tabela_headers = [ "Vôo", "custo","data"];
    let tabela_div = document.createElement('div');

    while(tabela_div.firstChild){
        tabela_div.removeChild(tabela_div.firstChild);
    }
    let tabela_visual = document.createElement('table');
    tabela_visual.className = "tabela";

    let tabela_header = document.createElement('thead');
    tabela_header.className = "tabela_head";

    let tabela_row = document.createElement('tr');
    tabela_row.className = "tabela_row";

    tabela_headers.forEach(header =>{
        let T_header = document.createElement('th');
        T_header.innerText = header
        tabela_row.append(T_header)
    })

    tabela_header.append(tabela_row);
    tabela_visual.append(tabela_header);

    let tabela_body = document.createElement('tbody')
    tabela_body.className = "Corpo-tabela"
    
    for (var i = 0; i < tamanho; i++) {
        let tabela_row2 = document.createElement('tr');
        tabela_row2.className = "tabela_row";
        let aux
        let cidadeTable = document.createElement('td')
        aux = path[i][0]
        cidadeTable.innerText = aux[0] +" -> " + aux[1]
        console.log(cidadeTable.innerText)
        let preçoTable = document.createElement('td')
        preçoTable.innerText = path[i][1]
        console.log(path[i][1])
        let dataTable = document.createElement('td')
        dataTable.innerText = path[i][2]
        console.log(path[i][2])

        tabela_row2.append(cidadeTable,preçoTable,dataTable)
        tabela_body.append(tabela_row2)
    }
    
    tabela_visual.append(tabela_body)
    tabela_div.append(tabela_visual)
    return tabela_div
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
    let loading = document.createElement('img')
    var gif = document.getElementById("div-gif");
    alert("Atualizando o pacote, isso pode demorar um pouco")
    gif.innerHTML += `<img src="https://flevix.com/wp-content/uploads/2019/07/Curve-Loading.gif" alt="funny GIF">`
    Http.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json_resp = JSON.parse(Http.responseText);
            if (json_resp.status_code===400) {
                alert(json_resp.detail);
                return;
            }
            gif.removeChild(gif.firstChild)
            alert('Pacote atualizado, procure por ele novamente para ver o resultado');

        }
    }
}