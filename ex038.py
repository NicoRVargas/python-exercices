num1, num2 =str(input("Digite dois valores inteiros: ")).split()
num1i = int(num1)
num2i = int(num2)

if num1i > num2i:
    print("O primeiro valor é o maior.")
elif num2i > num1i:
    print("O segundo valor é maior.")
else:
    print("Ambos os valores são iguais.")
    