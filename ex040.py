nota1, nota2 = input("Digite suas duas notas: ").split()
nota1n = float(nota1)
nota2n = float(nota2)
media = (nota1n + nota2n) / 2

if media < 5:
    print("Reprovado.")
elif 5 <= media < 6.9:
    print("Recuperação. Informe-se das datas.")
elif 10 >= media > 7:
    print("Aprovado. Parabéns.")
else:
    print("Notas digitadas incorretamente, tente novamente.")

    

