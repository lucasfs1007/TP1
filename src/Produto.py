from dataclasses import dataclass
from Categoria import Categoria
from Fornecedor import Fornecedor
from exceptions import CampoEmBrancoException, ValorInvalidoException


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
            raise CampoEmBrancoException('Nome não pode ser vazio')
        self.nome = nome
        if not descricao:
            raise CampoEmBrancoException('Descrição não pode ser vazio')
        self.descricao = descricao
        if not codigo_de_barras:
            raise CampoEmBrancoException('Código de barras não pode ser vazio')
        self.codigo_de_barras = codigo_de_barras
        if custo < 0:
            raise ValorInvalidoException('Custo não pode ser negativo')
        self.custo = custo
        if valor_venda < 0:
            raise ValorInvalidoException('Valor de venda não pode ser negativo')
        self.valor_venda = valor_venda
        self.categoria = categoria
        self.fornecedor = fornecedor
