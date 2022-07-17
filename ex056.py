media = 0
mulher_nova = 0
nome_velho = 0
idade_velho = 0
conta_homem = 0

quantidade = int(input("Digite o número de participantes: "))

print(15 * "-=")

for p in range(1, quantidade+1):
    nome = input(f"Digite o nome da {p}° pessoa: ")
    idade = int(input(f"Digite a idade da {p}° pessoa: "))
    sexo = input(f"Digite o sexo da {p}° pessoa[M/F]: ").upper()
    media += idade
    print(15 * "-=")

    if sexo == "M":
        if idade_velho < idade:
            idade_velho = idade
            nome_velho = nome
    if sexo == "F":
        if idade < 20:
            mulher_nova += 1

print(f"A média de idades dos integrantes é de {media/quantidade:.2f}\nO homem mais velho é {nome_velho}")
print(f"O número de mulheres com menos de 20 anos é de {mulher_nova}")





