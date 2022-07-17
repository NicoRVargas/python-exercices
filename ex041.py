from cProfile import run


idade = int(input("Insira sua idade: "))

if idade <= 9:
    print("Você está na categoria mirim.")
elif 9 < idade <= 14:
    print("Você está na categoria infantil.")
elif 14 < idade <= 19:
    print("Você está na categoria junior.")
elif 19 < idade <= 20:
    print("Você está na categoria sênior.")
elif idade > 20:
    print("Você está na categoria master.")
