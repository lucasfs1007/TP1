from dataclasses import dataclass
from Produto import Produto
from typing import List, Union

class Estoque:
    def __init__(self):
        self.produtos: List[Produto] = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def buscar_produto_por_nome(self, nome: str) -> Union[Produto, None]:
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def buscar_produto_por_codigo_de_barras(self, codigo: str) -> Union[Produto, None]:
        for produto in self.produtos:
            if produto.codigo_de_barras == codigo:
                return produto
        return None

