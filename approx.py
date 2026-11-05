import mpmath as mp

mp.mp.dps = int(input("Enter the amount of digit accuracy:"))

ans = int(input("What value would you like to approximate? (0 to quit, π=1, φ=2, e=3, √2=4): "))


def taylor():
    terms = int(input("How many terms: "))
    lis = []

    for i in range(terms):
        fact = mp.mpf(1) / mp.factorial(i)
        lis.append(fact)

    print(mp.nstr(mp.fsum(lis), n=mp.mp.dps))


def limit():
    x = int(input("What value?: "))

    result = (1 + mp.mpf(1) / x)**x

    print(mp.nstr(result, n=mp.mp.dps))


def generate_sequence():
    lis = [1, 2]

    a = int(input("How many terms of the fib sequence (starts with lis=[1,2]): "))

    for i in range(a):
        num = lis[-1] + lis[-2]
        lis.append(num)

    result = mp.mpf(lis[-1]) / lis[-2]

    print(mp.nstr(result, n=mp.mp.dps))


def Leibniz():
    lis = []

    a = int(input("How many terms?: "))

    for i in range(a):
        lis.append(mp.mpf(4) * (-1)**i / (2*i + 1))

    print(mp.nstr(mp.fsum(lis), n=mp.mp.dps))


if ans == 1:
    pi_ans = int(input("What method? (1 for Leibniz Formula): "))

    if pi_ans == 1:
        Leibniz()

elif ans == 2:
    generate_sequence()

elif ans == 3:
    e_ans = int(input("Which method? (1 for Taylor series, 2 for limit approximation): "))

    if e_ans == 1:
        taylor()

    elif e_ans == 2:
        limit()