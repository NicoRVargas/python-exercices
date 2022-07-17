aluno = {'nome': (input("Digite o nome do aluno: ")), 'media': (float(input("Insira a média do aluno: ")))}

print(f"O aluno {aluno['nome']},Teve a média {aluno['media']}")
if aluno['media'] > 7:
    print("Situação, Aprovado!")
else:
    print("Situação, reprovado.")
