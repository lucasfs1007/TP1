import pytest
from Transacao import Transacao, TipoTransacao, ValorInvalidoException
from Produto import Produto
from Categoria import Categoria
from Fornecedor import Fornecedor

class TestTransacao:
    tupla_teste = [
        (
            (
                "Sabão",
                "Mata 99.99%% dos germes.",
                "165316451165",
                2.0,
                2.5,
                ("Higiene",),
                ("Clebão Limpão", "61734620000149"),
            ),
            "VENDA",
            10,
            "Bradesco",
            "Banco do Brasil",
        ),
        (
            (
                "Teclado",
                "Teclado gamer da NASA",
                "165316459163",
                150.0,
                499.90,
                ("Eletrônico",),
                ("JamirGams", "92531901000128"),
            ),
            "AJUSTE_ESTOQUE",
            -10,
            "Loja 2",
            "Loja 1",
        ),
    ]

    @pytest.mark.parametrize(
        "produto_t,tipo_t,quantidade,origem,destino",
        tupla_teste,
    )
    def test_cadastro_transacao(
        self,
        produto_t: Produto,
        tipo_t: TipoTransacao,
        quantidade: int,
        origem: str,
        destino: str
    ):
        produto = Produto(*produto_t)
        tipo = TipoTransacao[tipo_t]
        transacao = Transacao(
            produto, tipo, quantidade, origem, destino
        )
        assert transacao is not None

    def test_cadastra_quantidade_valor_negativo_tipo_diferente_ajuste_estoque(self):
        with pytest.raises(ValorInvalidoException, match='Valor de quantidade para tipo de estoque diferente de Ajuste de estoque não pode ser negativo'):
            Transacao(
                Produto(                
                    "Sabão",
                    "Mata 99.99%% dos germes.",
                    "165316451165",
                    2.0,
                    2.5,
                    Categoria("Higiene"),
                    Fornecedor("Clebão Limpão", "61734620000149"),
                ),
                TipoTransacao.DEVOLUCAO,
                -5,
                "Loja 1",
                "Loja 2",
            )