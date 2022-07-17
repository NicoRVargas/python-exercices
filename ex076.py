'''lista = ("Mouse", 500, "Monitor", 1200, "Pc Gamer", 8900, "Mousepad", 150, "Teclado", 670)

print(25*"=")
print("Saldão Gamer")
print(25*"=")
print(lista[0], 15*"-", "R$", lista[1])
print(lista[2], 15*"-","R$", lista[3])
print(lista[4], 15*"-", "R$", lista[5])
print(lista[6], 15*"-", 'R$', lista[7])
print(lista[8], 15*"-", 'R$', lista[9])
print(25*"=")'''

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)
