from dataclasses import dataclass
from Produto import produto

class TipoTransacao(Enum):
    RECEBIMENTO = 'RECEBIMENTO'
    VENDA = 'VENDA'
    DEVOLUCAO = 'DEVOLUCAO'
    TRANSFERENCIA = 'TRANSFERENCIA'


@dataclass
class Transacao:
    produto: Produto
    tipo: TipoTransacao
    origem: str
    destino: str

def __init__(
        self,
        produto: Produto,
        tipo: TipoTransacao,
        origem: str,
        destino: float
    ):
        if not produto:
            raise ObjetoNuloException('Produto não pode ser nulo')
        self.produto = produto
        if not tipo:
            raise CampoEmBrancoException('Tipo nao pode ser nulo')
        self.tipo = tipo
        if not origem:
            raise CampoEmBrancoException('Origem não pode ser vazio')
        self.origem = origem
        if not destino:
            raise CampoEmBrancoException('Destino não pode ser vazio')
        self.destino = destino
