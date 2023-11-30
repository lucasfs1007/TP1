import pytest
from Produto import Produto, DescricaoEmBrancoException, ValorInvalidoException
from Categoria import Categoria
from Fornecedor import Fornecedor
from Estoque import Estoque

class TestEstoque:

    def test_adicionar_produto_ao_estoque(self):
        estoque = Estoque()
        produto = Produto(
            "Sabão",
            "Mata 99.99%% dos germes.",
            "165316451165",
            2.0,
            2.5,
            Categoria("Higiene"),
            Fornecedor("Clebão Limpão", "61734620000149"),
        )
        estoque.adicionar_produto(produto)
        assert len(estoque.produtos) == 1

    def test_buscar_produto_por_nome(self):
        estoque = Estoque()
        produto = Produto(
            "Sabão",
            "Mata 99.99%% dos germes.",
            "165316451165",
            2.0,
            2.5,
            Categoria("Higiene"),
            Fornecedor("Clebão Limpão", "61734620000149"),
        )
        estoque.adicionar_produto(produto)
        produto_encontrado = estoque.buscar_produto_por_nome("Sabão")
        assert produto_encontrado is not None
        assert produto_encontrado.nome == "Sabão"

    def test_buscar_produto_por_codigo_de_barras(self):
        estoque = Estoque()
        produto = Produto(
            "Sabão",
            "Mata 99.99%% dos germes.",
            "165316451165",
            2.0,
            2.5,
            Categoria("Higiene"),
            Fornecedor("Clebão Limpão", "61734620000149"),
        )
        estoque.adicionar_produto(produto)
        produto_encontrado = estoque.buscar_produto_por_codigo_de_barras("165316451165")
        assert produto_encontrado is not None
        assert produto_encontrado.codigo_de_barras == "165316451165"
