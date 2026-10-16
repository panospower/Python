num = 2.71
lis=[]
for digit in str(num):
    lis.append(digit)
    if digit == '.':
        lis.remove(digit)

if lis[-1] == '0':
    lis.remove(lis[-1])
print(len(lis))
