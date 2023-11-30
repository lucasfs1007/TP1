from dataclasses import dataclass
from Categoria import Categoria
from Fornecedor import Fornecedor


class DescricaoEmBrancoException(Exception):
    pass


class ValorInvalidoException(Exception):
    pass


@dataclass
class Produto:
    nome: str
    descricao: str
    codigo_de_barras: str
    custo: float
    valor_venda: float
    categoria: Categoria
    fornecedor: Fornecedor

    def __init__(
        self,
        nome: str,
        descricao: str,
        codigo_de_barras: str,
        custo: float,
        valor_venda: float,
        categoria: Categoria,
        fornecedor: Fornecedor,
    ):
        if not nome:
            raise DescricaoEmBrancoException()
        self.nome = nome
        if not descricao:
            raise DescricaoEmBrancoException()
        self.descricao = descricao
        if not codigo_de_barras:
            raise DescricaoEmBrancoException()
        self.codigo_de_barras = codigo_de_barras
        if custo < 0:
            raise ValorInvalidoException
        self.custo = custo
        if valor_venda < 0:
            raise ValorInvalidoException
        self.valor_venda = valor_venda
        self.categoria = categoria
        self.fornecedor = fornecedor
