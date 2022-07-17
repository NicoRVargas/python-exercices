listanomepeso = []
listageral = []
listapesada = []
listaleve = []
c = 0

while True:
    listanomepeso.append(input("Digite o seu nome: "))
    listanomepeso.append(int(input("Digite seu peso: ")))
    listageral.append(listanomepeso[:])
    listanomepeso.clear()
    opcao = input("Deseja continuar [S/N]: ").upper()
    if opcao == "S":
        continue
    if opcao == "N":
        break
    else:
        opcao = input("Deseja continuar [S/N]: ")

while c < len(listageral):
    if listageral[c][1] > 90:
        listapesada.append(listageral[c])
    c += 1
c = 0
while c < len(listageral):
    if listageral[c][1] < 50:
        listaleve.append([listageral[c]])
    c += 1

print(len(listageral))
print(listapesada)
print(listaleve)
