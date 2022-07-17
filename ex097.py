def escreva(txt):
    print(2 * len(txt) * "~~")
    print(f"{txt:^{4 * len(txt)}}")
    print(2 * len(txt) * "~~")


escreva("Gustavo")
escreva("Nicolas")
escreva("Tales")
escreva("cu")
