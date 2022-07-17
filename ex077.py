lista = ("Gaita", "Caderno", "Celular")

for p in range(0, len(lista)):
    if "A" or "E" or "I" or "O" or "U" in lista[p].upper():
        print(f"Na palavra {lista[p]} tem a vogal")
        if "a" in lista[p].lower(): print("A")
        if "e" in lista[p].lower(): print("E")
        if "i" in lista[p].lower(): print("I")
        if "o" in lista[p].lower(): print("O")
        if "u" in lista[p].lower(): print("U")
