#Regra de negócio, como será o comportamento do carrinho de compras

def criar_carrinho():
    '''
    Retorna o estado atual do carrinho
    total = Valor
    itens = Qauntidade de itens
    '''
    
    return {"total": 0, "itens": 0}

def adicionar_produto(carrinho, quantidade_desejada, estoque_disponivel, preco_unitario):
    '''
    Análise entre pedido e estoque
    '''
    
    if quantidade_desejada > estoque_disponivel:
        raise ValueError(f"Estoque insuficiente, possui apenas {estoque_disponivel} unidade/s")
    
    else:
        carrinho["itens"] += quantidade_desejada
        carrinho["total"] += quantidade_desejada * preco_unitario
