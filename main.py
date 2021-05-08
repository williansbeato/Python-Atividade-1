import produto

sair = 0

while sair != 6:
    print('\nCadastro de Produtos\n')
    print('1 - Cadastrar')
    print('2 - Buscar')
    print('3 - Editar')
    print('4 - Remover')
    print('0 - Sair')

    op = int(input("\nDigite a sua opção: "))

    if op == 1:
        with open(r"produtos.json") as arquivo:
            produto.createProduto(arquivo)
    elif op == 2:
        nome = input("\nDigite o nome do produto que deseja buscar: ")
        with open(r"produtos.json") as arquivo:
            produto.readProduto(arquivo, nome)
    elif op == 3:
        nome = input("Digite o nome do produto que deseja editar: ")
        with open(r"produtos.json") as arquivo:
            produto.updateProduto(arquivo, nome)
    elif op == 4:
        nome = input("Digite o nome do produto que deseja deletar: ")
        with open(r"produtos.json") as arquivo:
            produto.deleteProduto(arquivo, nome)
    elif op == 0:
        break