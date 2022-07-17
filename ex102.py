def fatorial(num, show=False):
    """
    CODE EXPLANATION:
    :paramter: num = Número para se fazer a fatorial.
    :paramter: show(opcional) = Se "False" mostra apenas resultado. Se "True" mostra conta.
    Função feita por Nico :).
    """
    f = 1
    if not show:
        while num > 0:
            f *= num
            num -= 1
        print(f)
    if show:
        for c in range(num, 0, -1):
            if c == 1:
                print(1, end=" ")
            else:
                print(f"{c} x ", end=" ")
        print("=", end=" ")
        while num > 0:
            f *= num
            num -= 1
        print(f)


help(fatorial)
fatorial(6, False)
