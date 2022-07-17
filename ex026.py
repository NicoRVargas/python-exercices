frase = str(input("Digite uma frase: ")).upper() .strip()
fraseA = frase.count("A")
fraseA1 = frase.find("A")
fraseAU = frase.rfind("A")

print(f"Nessa frase, temos {fraseA} quantidade de vezes que aparecem a letra ''a'', aparece pela primeira vez em {fraseA1} e por último em {fraseAU}")
