valores = input().split()

P, H = valores

P = int(P)
H = int(H)

if 0 < P < 1000 and 0 < H < 1000:
    calc = P / H
    print("{:.2f}".format(calc))