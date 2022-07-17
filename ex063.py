num = int(input("Digite o valor: "))
p = 0
s = 1
ps = p+s
c = 3
print("0 1", end=" ")

while c <= num:
    ps = p+s
    print(f"{ps}", end=" ")
    p = s
    s = ps
    c += 1
