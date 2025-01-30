window.onload = function(){ 
  const hostURL = window.location.origin;
  const loadingGif = document.getElementById("loadingGif");
  const searchButton = document.getElementById("searchButton");
  const responseContentJSONBox = document.getElementById("responseJSON");
  const responseContentHTMLBox = document.getElementById("responseHTML");
  const HTMLViewOptionButton = document.getElementById("htmlViewOption");
  const JSONViewOptionButton = document.getElementById("jsonViewOption");
  const textInput = document.getElementById("textInput");
  const responseStatusBox = document.getElementById("responseStatus");
  const nomeMedicamentoRadioButton = document.getElementById("nomeMedicamentoOption");
  const numeroProcessoRadioButton = document.getElementById("numeroProcessoOption");
  const dropdownMenuOptions = document.getElementById("dropdownMenu");
  const nextPageButton = document.getElementById("nextPageButton");
  const previousPageButton = document.getElementById("previousPageButton")
  const pageNumberDisplay = document.getElementById("pageNumberDisplay");
  let pageNumber = 1

  // query for medicine name on input typing
  textInput.addEventListener('input', async function() {
    if (nomeMedicamentoRadioButton.checked) { 
      if (textInput.value != "")  { 
        dropdownMenuOptions.innerHTML = ""
        const response = await fetch(`${hostURL}/medicines/available/${textInput.value}/`, { method: "GET" });
        const data = await response.json();
        for (let i = 0; i <= data.length; i++) {
          if (data[i] != undefined) {
            dropdownMenuOptions.innerHTML += `
              <li><a class="dropdown-item" href="#">${data["content"][i]}</a></li>
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

  // render http response
  function showResponseStatus(statusCode, message) {
    const boldElement = document.createElement('b');
    switch (statusCode) {
      case 200:
        boldElement.style.color = "#00b506";
        break;
      case 404:
        boldElement.style.color = "#de8d02";
        break;
      case 500:
        boldElement.style.color = "#b50000";
        break;
      default:
        boldElement.style.color = "#d7de02";
    };
    boldElement.textContent = ` HTTP ${statusCode} - ${message}`;
    responseStatusBox.appendChild(boldElement);
  }

  // render detailed medicine
  function renderHTMLView(data) {
    const medicamento = data["content"];
    responseContentHTMLBox.innerHTML = `
      <div class="d-flex gap-3 justify-content-between align-items-center">
        <img width="250" heigth="220" src="data:image/png;base64,${medicamento["imagemMedicamento"]}" alt="medicamento ${medicamento["nomeMedicamento"]}"/>
        <div>
          <b>ID medicamento: </b><span>${medicamento["medicamento"]["codigo"]}</span><br>
          <b>Número processo: </b><span>${medicamento["processo"]["numero"]}</span><br>
          <b>Nome medicamento: </b><span>${medicamento["medicamento"]["nome"]}</span><br>
          <b>Número registro: </b><span><a>${medicamento["medicamento"]["numeroRegistro"]}</a></span><br>
          <b>Data registro: </b><span><a>${medicamento["medicamento"]["dataRegistro"]}</a></span><br>
          <b>Data vencimento registro: </b><span><a>${medicamento["medicamento"]["dataVencimentoRegistro"]}</a></span><br>
          <b>Princípio ativo: </b><span><a>${medicamento["medicamento"]["principioAtivo"]}</a></span><br>
          <b>Nome Empresa farmacêutica: </b><span><a>${medicamento["empresaFarmaceutica"]["razaoSocial"]}</a></span><br>
          <b>CNPJ empresa farmacêutica: </b><span><a>${medicamento["empresaFarmaceutica"]["cnpj"]}</a></span><br>
          <a href="https://consultas.anvisa.gov.br/api/consulta/medicamentos/arquivo/bula/parecer/${medicamento["idBulaPaciente"]}/?Authorization=Guest" download>
            <img src="https://consultas.anvisa.gov.br/assets/img/pdf.png"/>  
            Download bula
          </a>
        </div>
      </div>
    `;
  }

  // render medicine
  function showData(data) {
    responseContentJSONBox.innerText = JSON.stringify(data, undefined, 2);
    if (numeroProcessoRadioButton.checked) {
      HTMLViewOptionButton.style.display = "unset";
      renderHTMLView(data);
    }
  }

  // fetch API data
  async function getData() {
    responseStatusBox.innerHTML = "Response status:";
    loadingGif.style.display = "unset";

    let params = { page: pageNumber }
    let query = `/?${new URLSearchParams(params).toString()}`;

    if (textInput.value != "") {
      if (nomeMedicamentoRadioButton.checked) {
        query = `/?search=${textInput.value}&${query}`;
      } else if (numeroProcessoRadioButton.checked) {
        query = `/${textInput.value}/`;
      }
    }

    try {
      const response = await fetch(`${hostURL}/medicines${query}`, { method: "GET" });
      const data = await response.json();
      showResponseStatus(data["code"], data["status"]);
      showData(data);
    } catch (error) {
      console.error(error.message);
    } finally {
      loadingGif.style.display = "none";
    }
  }

  // prevent default form event
  textInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      getData();
    }
  });

  // set buttons onclick functions
  function changePage(pageNumber) {
    pageNumberDisplay.innerText = `Página ${pageNumber}`;
    getData();
  }
  
  previousPageButton.onclick = function() {
    changePage(-1)
  };
  nextPageButton.onclick = function() {
    changePage(+1)
  };
  
  searchButton.onclick = function() {
    getData();
  }

  // switch view options
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

  getData();
};