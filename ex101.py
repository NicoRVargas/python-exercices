def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return "Não vota"
    if 18 > idade > 16:
        return "Voto opcional"
    if 65 > idade >= 18:
        return "Voto obrigatório"
    if idade >= 65:
        return "Voto opcional"


anon = int(input("Digite o ano do seu nascimento: "))

print(voto(anon))
