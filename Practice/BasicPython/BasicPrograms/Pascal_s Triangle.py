def n_choose_r(n, r, ncr=1):
    for i in range(1, r + 1):
        ncr *= (n - i + 1) / i
    return ncr


def whitespace(p, wsp=""):
    for j in range(1, p + 1):
        wsp += "  "
    return wsp


Index = int(input("Enter the Index of the Pascal's Triangle: "))

for k in range(0, Index + 1):
    print((whitespace(Index - k)), end="")
    for a in range(0, k + 1):
        print(int(n_choose_r(k, a)), end="")
        if a != k:
            print("  ", end="")
    print("\n", end="")
