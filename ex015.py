km = float(input('Quantos km você percorreu com o carro: '))
dias = int(input('E quantos dias você ficou com ele: '))
vkm = 0.15 * km
vdias = 60 * dias
vt = vkm + vdias

print(f'O valor total a pagar por km é de R${vkm}, já pelos dias é de R${vdias}, no total fica R${vt:.2f}')

