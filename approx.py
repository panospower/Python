import math

ans=int(input("What value would you like to approximate?(0 to quit ,π=1, φ=2, e=3, √2=4):"))


def taylor():
    terms = int(input("How many terms:"))
    lis=[]
    i=0
    while terms > i:
        fact = 1/math.factorial(i)
        lis.append(fact)
        i+=1
    print(sum(lis))

def limit():
    x=int(input("What value?:"))
    print((1+1/x)**x)

def generate_sequence():
    lis=[1,2]
    a=int(input("How many terms of the fib sequence(starts with lis=[1,2]):"))
    i=0
    while i < a:
        num=lis[-1]+lis[-2]
        lis.append(num)
        i+=1
    print(lis[-1]/lis[-2])


def Leibniz():
    lis=[]
    a = int(input("How many terms?:"))
    i=0
    while i < a:
        lis.append(4*((-1)**i)/(2*i+1))
        i+=1
    print(sum(lis))

if ans == 0:
    pass
if ans == 1:
    pi_ans=int(input("What method?(1 for Leibniz Formula(lowk sucks)):"))
    if pi_ans == 1:
        Leibniz()
if ans == 2:
    generate_sequence()
if ans == 3:
    e_ans=int(input("Which method?(1 for taylor series, 2 for limit approximation):"))
    if e_ans == 1:
        taylor()
    if e_ans == 2:
        limit()
    pass