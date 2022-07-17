import math
retaa, retab, retac = str(input("Insira três valores de retas: ")).split()
reta1 = float(retaa)
reta2 = float(retab)
reta3 = float(retac)

if (reta1 - reta2)**2 **1/2 < reta3 < (reta1 + reta2):
    print("Esses valores formam um triângulo ")
else:
    print("Esses valores não formam um triângulo")
    