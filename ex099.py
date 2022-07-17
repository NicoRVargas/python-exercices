def maior(*valores):
    print(f'Foram informados {len(valores)} valores.')
    print(f'Dentre os valores {valores}, {max(valores)} é o maior valor.')
    print('-' * 50)


maior(5, 4, 6, 9, 8)
maior(4, 5, 1)
maior(8, 17, 26, 51)
maior(0)
