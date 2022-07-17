from time import sleep
opcao = "S"
registro = {}
registros = []
idades = []
maiordeidade = []
contadorf = contadormi = 0

while opcao != "N":
    registro['nome'] = input("Insira seu nome: ").capitalize()
    registro['idade'] = idade = int(input("Insira sua idade: "))
    idades.append(registro['idade'])
    if idade >= 18:
        contadormi += 1
    sexo = input("Gênero [F/M]: ").upper()
    while sexo != "F" and sexo != "M":
        sexo = input("Gênero invalido.Digite novamente. [F/M]: ").upper()
    registro['sexo'] = sexo
    if sexo == "F":
        contadorf += 1
    opcao = input("Deseja continuar[S/N]: ").upper()
    while opcao != "S" and opcao != "N":
        opcao = input("Opção inválida tente novamente. [S/N]: ").upper()
    registros.append(registro.copy())

print(25 * "=-")
print(f"{'Registros Oficiais' :^50}")
print(25 * "=-")

print(f"{len(registros)} pessoa(s) foi(ram) registrada(s).")
print(f"A média de idades do grupo é {sum(idades)/len(idades):.2f}")

if contadorf != 0:
    print(12 * "=-")
    print(f"{'Mulheres' :^24}")
    print(12 * "=-")
    for c in range(0, len(registros)):
        if "F" in registros[c]['sexo']:
            print(f"{registros[c]['nome']}")
            sleep(1)
if contadorf == 0:
    print(12 * "=-")
    print(f"{'Nenhuma mulher registrada' :^24}")
    print(12 * "=-")

if contadormi != 0:
    print(12 * "=-")
    print(f"{'Maiores de Idade' :^24}")
    print(12 * "=-")
    for c in range(0, len(registros)):
        if registros[c]['idade'] >= 18:
            print(registros[c])
            sleep(1)
if contadormi == 0:
    print(12 * "=-")
    print(f"{'Nenhum maior de idade registrado' :^24}")
    print(12 * "=-")
