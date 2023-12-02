import pytest
from Produto import Produto, CampoEmBrancoException, ValorInvalidoException
from Categoria import Categoria
from Fornecedor import Fornecedor
from Estoque import Estoque


class TestEstoque:
    p1 = Produto(
        "Sabão de Banho",
        "Mata 99.99%% dos germes.",
        "165316451165",
        2.0,
        2.5,
        Categoria("Higiene"),
        Fornecedor("Clebão Limpão", "61734620000149"),
    )
    p2 = Produto(
        "Teclado",
        "Teclado gamer da NASA",
        "165316459163",
        150.0,
        499.90,
        Categoria("Eletrônico",),
        Fornecedor("JamirGams", "92531901000128"),
    )
    p3 = Produto(
        "Banheira",
        "Porcelana brilhosa!",
        "23342698238934986439728364",
        1000.0,
        1520.90,
        Categoria('Imóveis'),
        Fornecedor('PorceLaura', '13710697000136')
    )

    tupla_produtos = [
        [(p1,)],
        [(p1, p2)],
        [(p1, p2, p3)]
    ]
    
    @pytest.mark.parametrize('produtos', tupla_produtos)
    def test_adicionar_produtos_ao_estoque(self, produtos):
        estoque = Estoque()
        for p in produtos:
            estoque.adicionar_produto(p, 1)
        assert estoque.get_quantidade_produtos() == len(produtos)

    tupla_busca_por_nome = [
        ((p1, p2), 'Sabão', 1),  # produtos, query, quantidade_esperada
        ((p1, p2, p3), 'Banh', 2),
        ((p1, p2, p3), 'a', 3),
        ((p1, p3), 'Teclado', 0)
    ]

    @pytest.mark.parametrize('produtos,query,quantidade_esperada', tupla_busca_por_nome)
    def test_buscar_produto_por_nome(self, produtos, query, quantidade_esperada):
        estoque = Estoque()
        for p in produtos:
            estoque.adicionar_produto(p, 1)

        resultado = estoque.buscar_produtos_por_nome(query)
        assert len(resultado) == quantidade_esperada

    tupla_busca_por_codigo = [
        ((p1, p2), '165316451165', p1),  # produtos, query, produto_esperado
        ((p1, p2, p3), '23342698238934986439728364', p3),
        ((p2,), '165316459163', p2)
    ]

    @pytest.mark.parametrize('produtos,query,produto_esperado', tupla_busca_por_codigo)
    def test_buscar_produto_por_codigo_de_barras(self, produtos, query, produto_esperado):
        estoque = Estoque()
        for p in produtos:
            estoque.adicionar_produto(p, 1)
        
        resultado = estoque.buscar_produto_por_codigo_de_barras(query)
        assert resultado.produto == produto_esperado

    def test_buscar_produto_por_codigo_nao_existente(self):
        produtos = (TestEstoque.p1, TestEstoque.p2, TestEstoque.p3)
        query = '1234567890'
        estoque = Estoque()
        for p in produtos:
            estoque.adicionar_produto(p, 1)

        resultado = estoque.buscar_produto_por_codigo_de_barras(query)
        assert resultado is None
