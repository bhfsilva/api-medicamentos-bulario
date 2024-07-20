window.onload = function(){ 
  const loadingGif = document.getElementById("loadingGif");
  const botaoConsulta = document.getElementById("botaoConsulta");
  const responseContentJSONBox = document.getElementById("showResponseBodyJSON");
  const responseContentHTMLBox = document.getElementById("showResponseBodyHTML");
  const HTMLViewOptionButton = document.getElementById("htmlViewOption");
  const JSONViewOptionButton = document.getElementById("jsonViewoption");
  const inputTexto = document.getElementById("inputTexto");
  const responseStatusBox = document.getElementById("showResponseStatus");

  function showResponseStatus(responseStatus) {
    const boldElement = document.createElement('b');
    let httpCodeDescription = "";
    switch (responseStatus) {
      case 200:
        boldElement.style.color = "#00b506";
        httpCodeDescription = "OK";
        break;
      case 404:
        boldElement.style.color = "#de8d02";
        httpCodeDescription = "Not Found";
        break;
      default:
        boldElement.style.color = "#b50000";
        httpCodeDescription = "Internal Server Error";
    };

    boldElement.textContent = ` HTTP ${responseStatus} - ${httpCodeDescription}`;
    responseStatusBox.appendChild(boldElement);
  }

  function showData(data) {
    responseContentJSONBox.innerText = JSON.stringify(data, undefined, 2);
    renderHTMLoption(data);
  }

  async function getData() {
    responseStatusBox.innerHTML = "Response status:";
    loadingGif.style.display = "unset";

    try {
      const response = await fetch(`http://localhost:8080/medicamentos/?numeroProcesso=25351668917201032`, { method: "GET" });
      const data = await response.json();

      showResponseStatus(response.status);
      showData(data);

      if (data["content"][0]["medicamento"]["fotoMedicamentoBase64"] == "") {
        showData(data);
        getData();
      } else {
        loadingGif.style.display = "none";
        showData(data);
      }

    } catch (error) {
      loadingGif.style.display = "none";
      console.error(error.message);
    }
  }

  getData();

  inputTexto.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();
    }
  });

  botaoConsulta.onclick = function() {
    getData();
  }
  
  HTMLViewOptionButton.onclick = function() {
    responseContentJSONBox.style.display = "none";
    JSONViewOptionButton.disabled = false;
    responseContentHTMLBox.style.display = "unset";
    HTMLViewOptionButton.disabled = true;
  }

  JSONViewOptionButton.onclick = function() {
    responseContentJSONBox.style.display = "unset";
    JSONViewOptionButton.disabled = true;
    responseContentHTMLBox.style.display = "none";
    HTMLViewOptionButton.disabled = false;
  }

  function renderHTMLoption(data) {
    const medicamento = data["content"][0]["medicamento"];
    responseContentHTMLBox.innerHTML = `
      <div class="d-flex gap-3 justify-content-between align-items-center">
        <img width="250" heigth="220" src="data:image/png;base64,${medicamento["fotoMedicamentoBase64"]}" alt="medicamento ${medicamento["nomeMedicamento"]}"/>
        <div>
          <b>ID medicamento: </b><span>${medicamento["idMedicamento"]}</span><br>
          <b>Número processo: </b><span>${medicamento["numeroProcesso"]}</span><br>
          <b>Nome medicamento: </b><span>${medicamento["nomeMedicamento"]}</span><br>
          <b>Número registro: </b><span><a>${medicamento["numeroRegistro"]}</a></span><br>
          <b>Data registro: </b><span><a>${medicamento["dataRegistro"]}</a></span><br>
          <b>Data vencimento registro: </b><span><a>${medicamento["dataVencimentoRegistro"]}</a></span><br>
          <b>Princípio ativo: </b><span><a>${medicamento["principioAtivo"]}</a></span><br>
          <b>Nome Empresa farmacêutica: </b><span><a>${data["content"][0]["empresaFarmaceutica"]["razaoSocial"]}</a></span><br>
          <b>CNPJ empresa farmacêutica: </b><span><a>${data["content"][0]["empresaFarmaceutica"]["cnpj"]}</a></span><br>
          <a style="margin-top: 5px;" href="https://consultas.anvisa.gov.br/api/consulta/medicamentos/arquivo/bula/parecer/${medicamento["idBulaPaciente"]}/?Authorization=Guest" download>
            <img src="https://consultas.anvisa.gov.br/assets/img/pdf.png"/>  
            Download bula
          </a>
        </div>
      </div>
    `;
  }
};