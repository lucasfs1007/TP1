from dataclasses import dataclass
from Produto import Produto


@dataclass
class QuantidadeProduto:
    produto : Produto
    quantidade : int
