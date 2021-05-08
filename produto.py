import json

def createProduto(arquivo):
    produto = {
        "nome": input("\nDigite o nome: "), 
        "descricao": input("Digite a descricao: "),
        "preco": float(input("Digite o preco: R$"))
    }

    dados = json.load(arquivo)
    dados.append(produto)
    final = json.dumps(dados)
    arq = open(r"produtos.json", "w")
    arq.write(final)
   
def readProduto(arquivo, nome):
    dados = json.load(arquivo)
    for produto in dados:
        if produto["nome"] == nome:
            print("\nNome: {}".format(produto["nome"]))
            print("Descricao: {}".format(produto["descricao"]))
            print("Preco: R${}".format(produto["preco"]))
           
def updateProduto(arquivo, nome):
    dados = json.load(arquivo)
    for index, produto in enumerate(dados):
        if produto["nome"] == nome:
            dados.pop(index)

    produto = {
        "nome": input("\nDigite o nome: "), 
        "descricao": input("Digite a descricao: "),
        "preco": float(input("Digite o preco: R$"))
    }

    dados.append(produto)
    final = json.dumps(dados)
    arq = open(r"produtos.json", "w")
    arq.write(final)

def deleteProduto(arquivo, nome):
    dados = json.load(arquivo)
    for index, produto in enumerate(dados):
        if produto["nome"] == nome:
            dados.pop(index)

    final = json.dumps(dados)
    arq = open(r"produtos.json", "w")
    arq.write(final)
