# testo puro que deve ter as palavras
# Dado / Given -> estado inicial
# Quando / When -> ação do usuário
# Então / Then -> resultado
# texto deve ser igual no cód

Cenário: Adicionar produto com sucesso

    Dado que o carrinho está vazio, e o estoque possui 10 unidades do produto com preço de 5.00
    Quando eu adicionar 9 unidades ao carrinho
    Então o carrinho deve ter 9 itens
    E o valor total deve ser 45.00

  Cenário: Adicionar produto sem estoque

    Dado que o carrinho está vazio, e o estoque possui 1 unidades do produto com preço de 5.00
    Quando eu tento adicionar 2 unidades ao carrinho
    Então o sistema deve exibir a mensagem "Estoque insuficiente, possui apenas 1 unidade/s"




