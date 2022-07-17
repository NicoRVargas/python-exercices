salario = float(input("Digite seu salário: "))

if salario > 1250:
    print(f"{(salario / 100 * 10) + salario:.2f} é o seu novo salário")
else:
    print(f"{(salario / 100 * 15) + salario:.2f} é o seu novo salário")