import math
def SimpMethod2(func, args, a, b):
    EvenSum = 0
    OddSum = 0
    n = 10000  # Number of steps
    h = (b - a) / n  # Simpson rule step size
    s0 = func(a, args) + func(b, args)   # Sum for s0 term
    for i in range(1, n, 2):  # Sum for even values
        EvenSum += 2 * func(a + i * h, args)
    for i in range(2, n-1, 2):  # Sum for odd values
        OddSum += 4 * func(a + i * h, args)
    totalSum = EvenSum + OddSum + s0
    return (h / 3) * totalSum

def fz(args):
    m, u = args
    return (1 + (u ** 2 / m)) ** (-0.5 * (m + 1))

def Gfn(args):
    t, a = args
    return math.exp(-t) * (t ** (a-1))

def Km(m, a, b):
    alphaNum = 0.5 * m + 0.5
    alphaDenom = 0.5 * m
    j = Gamma(alphaNum, a, b)
    k = Gamma(alphaDenom, a, b)
    return j / (math.sqrt(m * math.pi) * k)

def Gamma(args):
    alpha, a, b = args
    if alpha % 1 == 0:
        j = 1
        for i in range(1, int(alpha)):
            j *= i
        return j
    j = SimpMethod2(Gfn, args, a, b)
    return j

def main():
    m = int(input("Enter the desired degrees of freedom (integer):"))
    b = float(input("Enter the upper integration boundary (float):"))
    a = b - 10 * b
    km = Km(m, a, b)
    z = SimpMethod2(fz, (m,), a, b)
    Fofz = km * z
    print("F(", z, ") =", Fofz)

if __name__ == "__main__":
    main()
