nome = input('Qual seu nome? ')

print('Qual o tipo primitivo desse valor?', type(nome))
print('É alfabético?', nome.isalpha)
print('É numérico? ', nome.isalnum)
print('Está em maiúsculo? ', nome.isupper)
print('Está em minúsculo? ', nome.islower)
print('Está capitalizada? ', nome.istitle)

# A parte do parenteses depois do isalpha é importante.
# exercício para uso dos "is", basicamente identificar o que é a variável.
