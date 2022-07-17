peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura**2

if imc < 18.5:
    print("Você é um anorexo.")
elif 18.5<=imc<25:
    print("Você tá dibas papai.")
elif 25<=imc<30:
    print("Tá comendo mta coxinha.")
elif 30<=imc<=40:
    print("PORRA MENÓ TU TÁ FODIDO.")
elif 40<imc:
    print("morreu.")