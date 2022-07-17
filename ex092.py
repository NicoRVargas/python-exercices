from datetime import datetime

cadastro = {'nome': input("insira seu nome: "),
            'idade': datetime.now().year - int(input("Digite o ano de seu nascimento: ")),
            'ctps': int(input("Carteira de trabalho[0 caso não tenha]: "))}

if cadastro['ctps'] != 0:
    cadastro['anocontrato'] = int(input("Em qual ano você começou a trabalhar: "))
    cadastro['salario'] = float(input("Qual seu salário: "))
    if datetime.now().year - cadastro['anocontrato'] < 35:
        cadastro['aposentadoria'] = (35 - (datetime.now().year - cadastro['anocontrato'])) + cadastro['idade']
    elif datetime.now().year - cadastro['anocontrato'] == 35:
        cadastro['aposentadoria'] = f"Você se aposenta esse ano! Parabéns e obrigado pela contribuição {cadastro['nome']} "
    elif datetime.now().year - cadastro['anocontrato']:
        cadastro['aposentadoria'] = "Você já está aposentado."

    print(f"""{cadastro['nome']} tem {cadastro['idade']} anos.
    o número do ctps é: {cadastro['ctps']}
    foi contratado em: {cadastro['anocontrato']}
    o salário é: {cadastro['salario']}
    vai se aposentar com: {cadastro['aposentadoria']}""")
elif cadastro['ctps'] == 0:
    print(f"""{cadastro['nome']} tem {cadastro['idade']} anos.
    ainda não trabalha.""")


