nomes = input("Digite seu nome: ") .strip()
nome = nomes.split()
nome1 = nome[0]
nomeu = nomes.count(' ')

print(f"primeiro nome: {nome1}\núltimo nome: {nome[nomes.count(' ')]}")