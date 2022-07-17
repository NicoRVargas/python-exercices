sexo = input("Qual seu sexo? [M/F]: ").upper().strip()
while sexo not in "MmFf":
    sexo = input("Não entendi, tente novamente: ")
print("Obrigado, informação computada.")
