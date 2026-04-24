# executa teste
import pytest
# "chamando" as funções para este file
from carrinho import criar_carrinho, adicionar_produto
# scenarios = escanea o .feature
# given, when, then  são os macadores dado(@given), quando (@when) e então (@then)
# parsers = traduz, transforma texto em "linguem .py"
from pytest_bdd import scenarios, given, when, then, parsers

# Conecta ao .feature
scenarios('carrinho.feature')

# Mantém estado do carrinho 
@pytest.fixture
def contexto():
    return {
        "carrinho": criar_carrinho(),
        "estoque": 0,
        "preco": 0.0,
        "erro": None
    }

# Segue o Gherkin

@given(parsers.parse('que o carrinho está vazio, e o estoque possui {qtd:d} unidades com preço {preco:f}'))
def inicializar_cenario(contexto, qtd, preco):
    contexto["carrinho"] = criar_carrinho()
    contexto["estoque"] = qtd
    contexto["preco"] = preco

@when(parsers.parse("adicionar {qtd:d} unidades"))
@when(parsers.parse("tentar adicionar {qtd:d} unidades"))
def executar_adicao(contexto, qtd):
    try:
        adicionar_produto(
            contexto["carrinho"], 
            qtd, 
            contexto["estoque"], 
            contexto["preco"]
        )
    except ValueError as e:
        contexto["erro"] = str(e)

@then(parsers.parse("carrinho deve ter {total_itens:d} itens"))
def verificar_itens(contexto, total_itens):
    assert contexto["carrinho"]["itens"] == total_itens

@then(parsers.parse("valor total deve ser {valor_total:f}"))
def verificar_valor(contexto, valor_total):
    assert contexto["carrinho"]["total"] == valor_total

@then(parsers.parse("sistema deve exibir a mensagem '{mensagem_esperada}'"))
def validar_mensagem_erro(contexto, mensagem_esperada):
    assert contexto["erro"] == mensagem_esperada
