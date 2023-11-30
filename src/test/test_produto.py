import pytest
from Produto import Produto, DescricaoEmBrancoException, ValorInvalidoException
from Categoria import Categoria
from Fornecedor import Fornecedor


class TestProduto:
    tupla_teste = [
        (
            "Sabão",
            "Mata 99.99%% dos germes.",
            "165316451165",
            2.0,
            2.5,
            ("Higiene",),
            ("Clebão Limpão", "61734620000149"),
        ),
        (
            "Teclado",
            "Teclado gamer da NASA",
            "165316459163",
            150.0,
            499.90,
            ("Eletrônico",),
            ("JamirGams", "92531901000128"),
        ),
    ]

    @pytest.mark.parametrize(
        "nome,descricao,codigo_de_barras,custo,valor_venda,categoria_t,fornecedor_t",
        tupla_teste,
    )
    def test_cadastro_produto(
        self,
        nome: str,
        descricao: str,
        codigo_de_barras: str,
        custo: float,
        valor_venda: float,
        categoria_t: Categoria,
        fornecedor_t: Fornecedor,
    ):
        categoria = Categoria(*categoria_t)
        fornecedor = Fornecedor(*fornecedor_t)
        produto = Produto(
            nome, descricao, codigo_de_barras, custo, valor_venda, categoria, fornecedor
        )
        assert produto is not None

    def test_cadastra_produto_nome_vazio(self):
        with pytest.raises(DescricaoEmBrancoException):
            Produto(
                "",
                "Docinho kkk!",
                "92531901001239",
                2.0,
                3.0,
                Categoria("Alimento"),
                Fornecedor("Nestle", "55056267000192"),
            )

    def test_cadastra_produto_descricao_vazia(self):
        with pytest.raises(DescricaoEmBrancoException):
            Produto(
                "Chocolate",
                "",
                "92531901001239",
                2.0,
                3.0,
                Categoria("Alimento"),
                Fornecedor("Nestle", "55056267000192"),
            )

    def test_cadastra_produto_codigo_de_barras_vazio(self):
        with pytest.raises(DescricaoEmBrancoException):
            Produto(
                "Chocolate",
                "Docinho kkk!",
                "",
                2.0,
                3.0,
                Categoria("Alimento"),
                Fornecedor("Nestle", "55056267000192"),
            )

    def test_cadastra_produto_custo_negativo(self):
        with pytest.raises(ValorInvalidoException):
            Produto(
                "Chocolate",
                "Docinho kkk!",
                "92531901001239",
                -2.0,
                3.0,
                Categoria("Alimento"),
                Fornecedor("Nestle", "55056267000192"),
            )

    def test_cadastra_produto_valor_negativo(self):
        with pytest.raises(ValorInvalidoException):
            Produto(
                "Chocolate",
                "Docinho kkk!",
                "92531901001239",
                2.0,
                -3.0,
                Categoria("Alimento"),
                Fornecedor("Nestle", "55056267000192"),
            )
