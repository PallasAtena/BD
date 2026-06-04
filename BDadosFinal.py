# Criei uma lista de dicionários porque facilita a iteração
# sequencial de todos os itens, a ordenação do estoque e segue
# o padrão estrutural amplamente utilizados nos APIs (JSON)


estoque = [
# Inseri as strings, a quantidade e os preços como em um estoque
    {"nome": "Notebook ASUS", "quantidade": 10, "preço": 3500.00},
    {"nome": "Mouse Wireless Logitec", "quantidade": 50, "preço": 89.90},
    {"nome": "Teclado Mecânico Adamantium", "quantidade": 25, "preço": 249.90},
]

# Inicia um laço de repetição infinito para manter o menu ativo
while True:
    # Exibe visualmente as opções disponíveis para o usuário
    print("\n--- MENU DE CONTROLE DE ESTOQUE ---")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")

    # Captura a escolha digitada pelo usuário no terminal
    opcao = input("Escolha uma opção (1-4): ")

    # OPÇÃO 1: Visualizar estoque detalhado
    if opcao == "1":
        print("\n--- ESTOQUE ATUAL ---")
        # Percorre cada dicionário de produto dentro da lista
        for produto in estoque:
            print(
                f"Produto: {produto['nome']} | "
                f"Qtd: {produto['quantidade']} | "
                f"Preço: R$ {produto['preço']:.2f}"
            )

    # OPÇÃO 2: Registrar entrada (somar estoque ou cadastrar novo)
    elif opcao == "2":
        print("\n--- REGISTRAR ENTRADA ---")
        nome_busca = input("Digite o nome do produto: ")

        # Busca se o produto já existe na lista
        produto_encontrado = False
        for produto in estoque:
            if produto["nome"].lower() == nome_busca.lower():
                qtd_entrada = int(input("Quantidade de entrada: "))
                # Atualiza a quantidade do item existente
                produto["quantidade"] += qtd_entrada
                print(f"Quantidade de '{produto['nome']}' atualizada!")
                produto_encontrado = True
                break

        # Se o produto não for encontrado, realiza o cadastro completo
        if not produto_encontrado:
            print(f"'{nome_busca}' não encontrado. Cadastrando novo produto...")
            qtd_inicial = int(input("Digite a quantidade inicial: "))
            preço_inicial = float(input("Digite o preço unitário: R$ "))

            # Cria um novo dicionário e adiciona à lista do estoque
            novo_produto = {
                "nome": nome_busca,
                "quantidade": qtd_inicial,
                "preço": preço_inicial
            }
            estoque.append(novo_produto)
            print(f"Produto '{nome_busca}' cadastrado com sucesso!")

    # OPÇÃO 3: Registrar saída (subtrair quantidade)
    elif opcao == "3":
        print("\n--- REGISTRAR SAÍDA ---")
        nome_busca = input("Digite o nome do produto: ")

        # Busca o produto correspondente na lista
        produto_encontrado = False
        for produto in estoque:
            if produto["nome"].lower() == nome_busca.lower():
                qtd_saida = int(input("Quantidade de saída: "))

                # Valida se há estoque suficiente para a saída
                if qtd_saida <= produto["quantidade"]:
                    # Atualiza a quantidade subtraindo o valor informado
                    produto["quantidade"] -= qtd_saida
                    print("Saída registrada com sucesso!")
                else:
                    print("Erro: Quantidade insuficiente em estoque.")

                produto_encontrado = True
                break

        if not produto_encontrado:
            print("Produto não encontrado no estoque.")

    # OPÇÃO 4: Verifica se o usuário escolheu a opção de encerramento
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        # Interrompe o laço while, finalizando a execução do programa
        break

    # Trata escolhas de opções inválidas no menu
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 4.")