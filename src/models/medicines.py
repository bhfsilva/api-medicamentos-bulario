from pydantic import BaseModel
from typing import Optional

class Medicine(BaseModel):
  idProduto: Optional[int]
  numeroRegistro: Optional[str]
  nomeProduto: Optional[str]
  expediente: Optional[str]
  razaoSocial: Optional[str]
  cnpj: Optional[str]
  numeroTransacao: Optional[str]
  data: Optional[str]
  numProcesso: Optional[str]
  idBulaPacienteProtegido: Optional[str]
  idBulaProfissionalProtegido: Optional[str]
  dataAtualizacao: Optional[str]

class Process(BaseModel):
  numero: Optional[str]
  situacao: Optional[int]
  numeroProcessoFormatado: Optional[str]

class Type(BaseModel):
  codigo: Optional[int]
  descricao: Optional[str]

class RegulatoryCategory(BaseModel):
  codigo: Optional[int]
  descricao: Optional[str]

class Product(BaseModel):  
  codigo: Optional[int]
  nome: Optional[str]
  numeroRegistro: Optional[str]
  tipo: Type
  categoria: Optional[str]
  situacaoRotulo: Optional[str]
  dataVencimento: Optional[str]
  mesAnoVencimento: Optional[str]
  dataVencimentoRegistro: Optional[str]
  principioAtivo: Optional[str]
  situacaoApresentacao: Optional[str]
  dataRegistro: Optional[str]
  categoriaRegulatoria: RegulatoryCategory
  medicamentoReferencia: Optional[str]
  categoriaProduto: Optional[str]
  complemento: Optional[str]
  tipoAutorizacao: Optional[str]
  tipoPriorizacao: Optional[str]
  descricaoMedicamentoNotificado: Optional[str]
  categoriaMedicamentoNotificado: Optional[str]
  codigoNotificacao: Optional[int]
  sinonimos: Optional[str]
  indicacoes: Optional[str]
  dataCancelamento: Optional[str]
  numeroRegistroFormatado: Optional[str]
  mesAnoVencimentoFormatado: Optional[str]
  acancelar: Optional[bool]
  
class Enterprise(BaseModel):
  cnpj: Optional[str]
  razaoSocial: Optional[str]
  numeroAutorizacao: Optional[str]
  cnpjFormatado: Optional[str]

class DetailedMedicine(BaseModel):
  ordem: Optional[int]
  imagemMedicamento: Optional[str]
  idBulaPaciente: Optional[str]
  idBulaProfissional: Optional[str]
  medicamento: Product
  empresaFarmaceutica: Enterprise
  processo: Process
        