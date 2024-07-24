window.onload = function(){ 
  const loadingGif = document.getElementById("loadingGif");
  const searchButton = document.getElementById("searchButton");
  const responseContentJSONBox = document.getElementById("responseJSON");
  const responseContentHTMLBox = document.getElementById("responseHTML");
  const HTMLViewOptionButton = document.getElementById("htmlViewOption");
  const JSONViewOptionButton = document.getElementById("jsonViewoption");
  const textInput = document.getElementById("textInput");
  const responseStatusBox = document.getElementById("responseStatus");
  const nomeMedicamentoRadioButton = document.getElementById("nomeMedicamentoOption");
  const numeroProcessoRadioButton = document.getElementById("numeroProcessoOption");
  const dropdownMenuOptions = document.getElementById("dropdownMenu");

  textInput.addEventListener('input', async function() {
    if (nomeMedicamentoRadioButton.checked) { 
      if (textInput.value != "")  { 
        dropdownMenuOptions.innerHTML = ""
        const response = await fetch(`http://localhost:8080/medicamentos/disponiveis/${textInput.value}/`, { method: "GET" });
        const data = await response.json();
        for (let i = 0; i <= data.length; i++) {
          if (data[i] != undefined) {
            dropdownMenuOptions.innerHTML += `
              <li><a class="dropdown-item" href="#">${data[i]}</a></li>
            `;
          }
        }
        dropdownMenuOptions.classList.remove('show');
        if (data.length != 0) {
          dropdownMenuOptions.classList.add('show');
        }
      } else {
        dropdownMenuOptions.classList.remove('show');
      }
    }
    dropdownMenuOptions.querySelectorAll('a').forEach(dropdownOption => {
      dropdownOption.addEventListener('click', function() {
        textInput.value = dropdownOption.innerText;
        dropdownMenuOptions.classList.remove('show');
      });
    });
  });

  function showResponseStatus(responseStatus) {
    const boldElement = document.createElement('b');
    let httpCodeDescription = "";
    console.log(responseStatus)
    switch (responseStatus) {
      case 200:
        boldElement.style.color = "#00b506";
        httpCodeDescription = "OK";
        break;
      case 404:
        boldElement.style.color = "#de8d02";
        httpCodeDescription = "Not Found";
        break;
      case 500:
        boldElement.style.color = "#b50000";
        httpCodeDescription = "Internal Server Error";
        break;
      default:
        boldElement.style.color = "#d7de02";
        httpCodeDescription = "Partial Content";
    };
    boldElement.textContent = ` HTTP ${responseStatus} - ${httpCodeDescription}`;
    responseStatusBox.appendChild(boldElement);
  }

  function renderHTMLView(data) {
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
          <a href="https://consultas.anvisa.gov.br/api/consulta/medicamentos/arquivo/bula/parecer/${medicamento["idBulaPaciente"]}/?Authorization=Guest" download>
            <img src="https://consultas.anvisa.gov.br/assets/img/pdf.png"/>  
            Download bula
          </a>
        </div>
      </div>
    `;
  }

  function showData(data) {
    responseContentJSONBox.innerText = JSON.stringify(data, undefined, 2);
    if (numeroProcessoRadioButton.checked) {
      HTMLViewOptionButton.style.display = "unset";
      renderHTMLView(data);
    }
  }

  async function getData() {
    responseStatusBox.innerHTML = "Response status:";
    loadingGif.style.display = "unset";

    let query = "";

    if (textInput.value != "") { 
      if (nomeMedicamentoRadioButton.checked) {
        query = `/${textInput.value}/`;
      } else if (numeroProcessoRadioButton.checked) {
        query = `/?numeroProcesso=${textInput.value}`;
      }
    }

    try {
      const response = await fetch(`http://localhost:8080/medicamentos${query}`, { method: "GET" });
      const data = await response.json();
      showResponseStatus(response.status);
      showData(data);
      if (numeroProcessoRadioButton.checked) {
        if (data["content"][0]["medicamento"]["fotoMedicamentoBase64"] == "") {
          showData(data);
          getData();
        } else {
          showData(data);
        }
      }
      loadingGif.style.display = "none";
    } catch (error) {
      loadingGif.style.display = "none";
      console.error(error.message);
    }
  }

  getData();

  textInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      getData();
    }
  });

  searchButton.onclick = function() {
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
};