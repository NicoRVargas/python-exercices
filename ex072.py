numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
num = int(input("Digite um número de 0 a 10: "))
while num not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    num = int(input("Não entendi. Digite um número de 0 a 10: "))
print(f"O número {num} escrito por extenso é {numeros[num].upper()}.")
