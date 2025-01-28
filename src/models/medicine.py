from pydantic import BaseModel
from typing import Optional

class Medicine(BaseModel):
  idProduto: int
  numeroRegistro: str
  nomeProduto: str
  expediente: str
  razaoSocial: str
  cnpj: str
  numeroTransacao: str
  data: str
  numProcesso: str
  idBulaPacienteProtegido: str
  idBulaProfissionalProtegido: str
  dataAtualizacao: str

class Process(BaseModel):
  numero: str
  situacao: int
  numeroProcessoFormatado: str

class Type(BaseModel):
  codigo: int
  descricao: Optional[str]

class RegulatoryCategory(BaseModel):
  codigo: int
  descricao: str

class Product(BaseModel):  
  codigo: int
  nome: str
  numeroRegistro: str
  tipo: Type
  categoria: Optional[str]
  situacaoRotulo: Optional[str]
  dataVencimento: Optional[str]
  mesAnoVencimento: str
  dataVencimentoRegistro: str
  principioAtivo: str
  situacaoApresentacao: str
  dataRegistro: str
  categoriaRegulatoria: RegulatoryCategory
  medicamentoReferencia: str
  categoriaProduto: Optional[str]
  complemento: Optional[str]
  tipoAutorizacao: str
  tipoPriorizacao: Optional[str]
  descricaoMedicamentoNotificado: Optional[str]
  categoriaMedicamentoNotificado: str
  codigoNotificacao: int
  sinonimos: str
  indicacoes: str
  dataCancelamento: Optional[str]
  numeroRegistroFormatado: str
  mesAnoVencimentoFormatado: str
  acancelar: bool
  
class Enterprise(BaseModel):
  cnpj: str
  razaoSocial: str
  numeroAutorizacao: str
  cnpjFormatado: str

class DetailedMedicine(BaseModel):
  ordem: int
  imagem: str
  produto: Product
  empresa: Enterprise
  processo: Process
        