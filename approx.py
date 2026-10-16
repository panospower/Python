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

if ans == 0:
    pass
if ans == 3:
    e_ans=int(input("Which way?(1 for taylor series, 2 for series approximation):"))
    if e_ans == 1:
        taylor()
    if e_ans == 2:
        pass
    pass