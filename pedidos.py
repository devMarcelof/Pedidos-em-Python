pedidos = []

# Função para adicionar itens ao pedido
def adicionar_item_pedido():
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    return {'nome_produto': nome_produto, 'quantidade': quantidade, 'valor_unitario': valor_unitario}

# Função para calcular o valor
def calcular_valor_pedido(itens):
    valor_total = sum(item['quantidade'] * item['valor_unitario'] for item in itens)
    frete = 0 if valor_total >= 500 else valor_total * 0.1
    return valor_total, frete, valor_total + frete

while True:
    nome_cliente = input("Informe o Nome do cliente (ou 'sair' para encerrar): ")
    if nome_cliente.lower() == 'sair':
        break

    data_pedido = input("Informe a data do pedido: ")
    
    resposta_fidelidade = 0
    while resposta_fidelidade != 1 and resposta_fidelidade != 2:
        resposta_fidelidade = int(input("O cliente participa do programa de fidelidade? Digite '1' para sim, '2' para não: "))
        if resposta_fidelidade == 1:
            possui_fidelidade = True
        elif resposta_fidelidade == 2:
            possui_fidelidade = False
        else:
            print("Valor inválido! ")

    lista_itens_pedido = []
    while True:
        novo_item = adicionar_item_pedido()
        lista_itens_pedido.append(novo_item)

        continuar = input("Deseja adicionar mais um item ao pedido? Digite 's' para Sim ou Digite 'n' para Não: ")
        if continuar.lower() != 's':
            break

    valor_itens, valor_frete, valor_total_pedido = calcular_valor_pedido(lista_itens_pedido)

    pedido = {
        'nome_cliente': nome_cliente,
        'data_pedido': data_pedido,
        'possui_fidelidade': possui_fidelidade,
        'itens_pedido': lista_itens_pedido,
        'valor_itens': valor_itens,
        'valor_frete': valor_frete,
        'valor_total_pedido': valor_total_pedido
    }
    pedidos.append(pedido)

# Utilização do for para imprimir os pedidos
for pedido in pedidos:
    print("\nResumo do Pedido:")
    print(f"Nome do cliente: {pedido['nome_cliente']}")
    print(f"Valor somado dos itens do pedido: R$ {pedido['valor_itens']:.2f}")
    print(f"Valor do frete: R$ {pedido['valor_frete']:.2f}")
    print(f"Valor total do pedido: R$ {pedido['valor_total_pedido']:.2f}")
