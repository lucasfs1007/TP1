from dataclasses import dataclass, field
from QuantidadeProduto import QuantidadeProduto
from Produto import Produto
from typing import List, Union


@dataclass
class Estoque:
    _produtos: List[QuantidadeProduto] = field(default_factory=list, init=False)

    def adicionar_produto(self, produto: Produto, quantidade_inicial) -> None:
        self._produtos.append(QuantidadeProduto(produto, quantidade_inicial))

    def get_quantidade_produtos(self) -> int:
        return len(self._produtos)

    def buscar_produtos_por_nome(self, nome: str) -> List[QuantidadeProduto]:
        return [qp for qp in self._produtos if nome in qp.produto.nome]

    def buscar_produto_por_codigo_de_barras(self, codigo: str) -> QuantidadeProduto | None:
        for qp in self._produtos:
            if qp.produto.codigo_de_barras == codigo:
                return qp
        return None
    
    def __iter__(self):
        for p in self._produtos:
            yield p
