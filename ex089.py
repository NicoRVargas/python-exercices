listanome = []
listanotas = []
opcao = "S"

while opcao == "S":
    listanome.append(input("Insira o nome do aluno: ").capitalize())

    nota1 = (float(input("Primeira nota: ")))
    nota2 = (float(input("Segunda nota: ")))

    listanotas.append([nota1, nota2])

    opcao = input("Deseja continuar[S/N]: ").upper()
    while opcao != "N" and opcao != "S":
        opcao = input("Não entendi. Deseja continuar[S/N]: ").upper()

print(25*"=-")
print(f"No.  Nome.   Média.")
print(25*"-")
for c in range(0, len(listanome)):
    print(f"{c}   {listanome[c]:^8}      {(listanotas[c][0] + listanotas[c][1]) / 2:<8}")
print(25*"-")

while opcao != 999:
    opcao = int(input("Qual aluno você quer ver a nota [999 para sair]: "))

    while opcao != 999 and opcao >= len(listanome) or opcao < 0:
        print("Lembrando. Para sair digite [999].")
        opcao = int(input("Não entendi. Qual aluno você quer ver a nota [999]: "))

    if opcao != 999:
        print(f"Notas de {listanome[opcao]} são {listanotas[opcao]}")
