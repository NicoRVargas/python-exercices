times = ("Bahia", "Cruzeiro", "Sport Recife", "Grêmio IMORTAL", "Vasco", "Chapecoense", "Novorizontino", "Operário",
"Ituano", "Ponte Preta", "Náutico", "Brusque", "Vila Nova", "Criciúma", "CSA", "Guarani", "Sampaio Corrêa", "Londrina",
"Tombense", "CRB")
print(f"Os 5 primeiros colocados do BRASILEIRÃO B 2022 são: {times[:5]}")
print(f"O Z4 desse BRASILEIRÃO B 2022 é: {times[-4:]}")
print(f"A tabela por ordem alfabética é {sorted(times)}")
print(f"A Chapecoense está na posição {times.index('Chapecoense')+1}")