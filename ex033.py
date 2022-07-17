num, num2, num3 = str(input("Insira três números: ")).split()

numi = int(num)
numi2 = int(num2)
numi3 = int(num3)

if numi > numi2 > numi3:
    print(f"{numi} é o maior número, já o {numi3} é o menor.")
if numi > numi3 > numi2:
    print(f"{numi} é o maior número, já o {numi2} é o menor.")
if numi2 > numi3 > numi:
    print(f"{numi2} é o maior número, já o {numi} é o menor.")
if numi2 > numi > numi3:
    print(f"{numi2} é o maior, já o {numi3} é o menor.")
if numi3 > numi2 > numi:
    print(f"{numi3} é o maior, já o menor é {numi}")
if numi3 > numi > numi2:
    print(f"{numi3} é o maior, já o menor é {numi2}")

