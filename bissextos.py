ano = int(input('que ano quer analisar?'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f"ano {ano} é bisexto")
else:
    print(f"ano {ano} NAO é bisexto")    
