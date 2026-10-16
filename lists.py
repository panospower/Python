import math

digits = int(input("How many digits: "))
lis=[]
i = 0
while digits > i:
    fact = 1/math.factorial(i)
    lis.append(fact)
    print(len(str(fact))-1)
    i+=1

print(sum(lis))