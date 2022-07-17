idade = idade_mulher_jovem = contador_mulher_jovem = contador_homens = contador_maior_de_idade = 0

print("="*10, "Cadastro de Pessoas", "="*10)

while True:
    idade = int(input("Digite Sua idade: "))
    genero = input("Digite seu gênero, [M/F]: ").upper()
    while genero not in "MF":
        genero = input("Desculpe não entendi. Digite seu gênero, [M/F]: ").upper()
    if idade >= 18:
        contador_maior_de_idade += 1
    if genero == "F".upper():
        if idade < 20:
            contador_mulher_jovem += 1
    if genero == "M".upper():
        contador_homens += 1
    opcao = input("Deseja continuar[S/N]? ").upper()
    while opcao not in "SN":
        opcao = input("Desculpe, não entendi. Deseja continuar[S/N]? ").upper()
    if opcao == "N".upper():
        break

print(10*"=", "Resultados", 10*"=")
print(f"""Tem {contador_maior_de_idade} maiores de idade nessa lista.
Há {contador_homens} homens.
{contador_mulher_jovem} mulher(res) com menos de 20 anos.""")
print(32 * "=")