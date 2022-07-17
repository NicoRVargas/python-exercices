velocidade = float(input("Insira a velocidade do carro: "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print("Você foi multado por excesso de velocidade. Irei imprimir o valor de sua multa.")
    print(f"Este é o valor de sua multa R${multa:.2f}.")
else:
    print("Você está dentro dos limites permitidos, pode ir.")

