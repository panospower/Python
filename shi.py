import math

def taylor_series():
    terms = int(input("How many terms:"))
    lis=[]
    i = 0
    while terms > i:
        fact = 1/math.factorial(i)
        lis.append(fact)
        i+=1
    
    print(sum(lis))

def digit_counter():
    num = 2.71250
    lis=[]
    for digit in str(num):
        lis.append(digit)
        if digit == '.':
            lis.remove(digit)

    if lis[-1] == '0':
        lis.remove(lis[-1])
    print(len(lis))
