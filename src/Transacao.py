from dataclasses import dataclass
from enum import Enum
from Produto import Produto
from exceptions import ValorInvalidoException 

class TipoTransacao(Enum):
    RECEBIMENTO = 'RECEBIMENTO'
    VENDA = 'VENDA'
    DEVOLUCAO = 'DEVOLUCAO'
    TRANSFERENCIA = 'TRANSFERENCIA'
    AJUSTE_ESTOQUE = 'AJUSTE_ESTOQUE'


@dataclass
class Transacao:
    produto: Produto
    tipo: TipoTransacao
    quantidade: int
    origem: str
    destino: str

    def __init__(
            self,
            produto: Produto,
            tipo: TipoTransacao,
            quantidade: int,
            origem: str,
            destino: str
        ):
            self.produto = produto
            if quantidade < 0 and tipo != TipoTransacao.AJUSTE_ESTOQUE:
                raise ValorInvalidoException('Valor de quantidade para tipo de estoque diferente de Ajuste de estoque não pode ser negativo')
            self.quantidade = quantidade
            self.tipo = tipo
            self.origem = origem
            self.destino = destino
