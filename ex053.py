frase = input("Digite uma frase: ").strip().upper()
lista_palavras = frase.split()
palavras_juntas = "".join(lista_palavras)
frase_reversa = palavras_juntas[::-1]
if palavras_juntas == frase_reversa:
    print("Esta é uma frase palíndroma.")
else:
    print("Esta não é uma frase palíndroma.")
