# API Medicamentos Bulário

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

<div align="center">
  
  ![api-med](https://github.com/user-attachments/assets/9252f686-0638-4df3-88d8-ca090516578d)
  <br>*Consulta ao medicamento AAS retornando imagem*
</div>

## 📝 Sobre o projeto

* Projeto pessoal;
* Realiza consultas à API de bulário da ANVISA, retornando informações sobre medicamentos incluindo uma imagem em formato base 64;
* Por se tratar de uma API que retorna imagens há também um visualizador de respostas da API feito em JavaScript Vanilla;
  * Esse visualizador pode ser acessado pela rota `/visualizer`.
* <strong>Tecnologias usadas na API</strong>: `🐍 Python 3`, `⚡ FastAPI`, `✅ Selenium`;
* <strong>Tecnologias usadas no visualizador</strong>: `🟪 Bootstrap`, `🟨 JavaScript`.

> [!IMPORTANT]
> A extração das imagens é feita utilizando Selenium, capturando o base 64 das imagems retornadas em uma busca no Google Imagens. Por essa razão, podem haver diferenças entre o medicamento consultado e a imagem retornada.

## Endpoints
### GET /docs
Acessa página com documentação gerada pelo Swagger.
### GET /visualizer
Acessa cliente para consulta das informações e visualização das imagens dos medicamentos.
### GET /medicines
Retorna página contendo lista de medicamentos simples em ordem alfabética.
### GET /medicines/available/{nome do medicamento}
Retorna lista de strings contendo o nome dos medicamentos disponíveis para consulta.
### GET /medicines/{número do processo do medicamento}
Retorna medicamento completo incluindo sua imagem no formato base 64.
## Query Params
### GET /medicines/{número do processo do medicamento}/?index={index da imagem}
Altera a imagem retornada baseando-se na posição da imagem no Google Imagens (por padrão a primeira imagem é retornada).
> [!TIP]
> O termo buscado no Google Imagens para captura da imagem é: <b>"medicamento" + {nome do medicamento} + {razão social da empresa farmacêutica}<b>
### GET /medicines/?search={nome do medicamento}
Retorna página contendo lista de medicamentos simples com o mesmo nome porém de diferentes empresas farmacêuticas.
### GET /medicines/?size={quantidade de medicamentos}
Limita quantidade de medicamentos retornados (por padrão 5 medicamentos são retornados).
### GET /medicines/?page={quantidade de medicamentos}
Consulta nova página de medicamentos.

## Modelos
### Medicamento simples
```python
{
  "idProduto": int
  "numeroRegistro": str
  "nomeProduto": str
  "expediente": str
  "razaoSocial": str
  "cnpj": str
  "numeroTransacao": str
  "data": str
  "numProcesso": str
  "idBulaPacienteProtegido": str
  "idBulaProfissionalProtegido": str
  "dataAtualizacao": str
}
```
### Medicamento completo
```python
{
  "ordem": int
  "imagemMedicamento": str
  "idBulaPaciente": str
  "idBulaProfissional": str
  "medicamento": {
    "codigo": int
    "nome": str
    "numeroRegistro": str
    "tipo": {
      "codigo": int
      "descricao": Optional[str]
    }
    "categoria": Optional[str]
    "situacaoRotulo": Optional[str]
    "dataVencimento": Optional[str]
    "mesAnoVencimento": str
    "dataVencimentoRegistro": str
    "principioAtivo": str
    "situacaoApresentacao": str
    "dataRegistro": str
    "categoriaRegulatoria": {
      "codigo": int
      "descricao": str
    }
    "medicamentoReferencia": str
    "categoriaProduto": Optional[str]
    "complemento": Optional[str]
    "tipoAutorizacao": str
    "tipoPriorizacao": Optional[str]
    "descricaoMedicamentoNotificado": Optional[str]
    "categoriaMedicamentoNotificado": str
    "codigoNotificacao": int
    "sinonimos": str
    "indicacoes": str
    "dataCancelamento": Optional[str]
    "numeroRegistroFormatado": str
    "mesAnoVencimentoFormatado": str
    "acancelar": boolean
  }
  "empresaFarmaceutica": {
    "cnpj": str
    "razaoSocial": str
    "numeroAutorizacao": str
    "cnpjFormatado": str
  }
  "processo": {
    "numero": str
    "situacao": int
    "numeroProcessoFormatado": str
  }
}
```
