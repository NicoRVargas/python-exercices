largP = float(input('Largura da parede: '))
altP = float(input('Altura da parede: '))
areaP = largP * altP
tinta = areaP // 2
tinta2 = areaP % 2

if tinta2 != 0:
    print(f'{tinta2 ** 0 + tinta}')
else:
    print(f'{tinta}')


