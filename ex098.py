from time import sleep


def contador(inicio, fim, passo):

    while inicio != fim:
        if passo == 0:
            passo = 1
        if inicio > fim:
            print(inicio)
            sleep(0.4)
            inicio -= passo
        else:
            if inicio + passo > fim:
                break
            print(inicio)
            sleep(0.4)
            inicio += passo

    print(25 * "~~")


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input("Digite o valor inicial: ")),
         int(input("Digite o valor final: ")),
         int(input("Digite o valor final: ")))

