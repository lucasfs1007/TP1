from dataclasses import dataclass
from Produto import Produto
from typing import List, Union

@dataclass
class Estoque:
    produtos: List[Produto]

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def buscar_produto_por_nome(self, nome: str) -> Union[dict, None]:
        resultados = {}
        for produto in self.produtos:
            if produto.nome == nome:
                resultados[produto] = resultados.get(produto, 0) + 1
        return resultados if resultados else None

    def buscar_produto_por_codigo_de_barras(self, codigo: str) -> Union[dict, None]:
        resultados = {}
        for produto in self.produtos:
            if produto.codigo_de_barras == codigo:
                resultados[produto] = resultados.get(produto, 0) + 1
        return resultados if resultados else None
