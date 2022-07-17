def notas(*num, situation=False):
    alunos = {"notas": num}
    soma = 0
    print(f'Número de notas: {len(alunos["notas"][0])}')
    print(f'Menor nota: {sorted(alunos["notas"][0])[0]}')
    print(f'Maior nota: {sorted(alunos["notas"][0])[-1]}')
    for nota in alunos["notas"][0]:
        soma += nota
    resultado = soma / len(alunos["notas"][0])
    print(f"Média da turma: {resultado:.2f}")
    if situation:
        if resultado >= 7:
            print("Situação Boa")
        else:
            print("Situação Ruim")
    if not situation:
        print("Para saber a situação, coloque True")


r = 2, 4, 5, 6, 4, 2, 9
notas(r, situation=True)

