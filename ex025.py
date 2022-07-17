import datetime
from time import sleep
nome = str(input("Digite seu nome completo: ")).upper() .strip()

print("Analisando se no seu nome tem Silva...")
sleep(3)
print("SILVA" in nome)

