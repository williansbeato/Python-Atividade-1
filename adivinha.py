import random

num_secreto = random.randint(1,10)

palpite = 0

while palpite != num_secreto:
    
    palpite = int(input("\nDigite um numero entre 1 a 10: "))

    if palpite > num_secreto:
        print("\nNumero Errado!")
        print("\nNumero menor que", palpite)
    elif palpite < num_secreto:
        print("\nPalpite Errado!")
        print("\nNumero maior que", palpite)
    else:
        print("\nParabens! O numero era ", num_secreto)
