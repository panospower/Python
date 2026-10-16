from random import randint

nums=[]
list_accuracy=[]
size=int(input("How many nums:"))
amount=int(input("How many attempts:"))
i=0
while i < size:
   nums.append(0)
   i+=1
i=0
while i < amount:
    n=randint(0,size-1)
    nums[n]+=1
    i+=1
i=0
print(nums)
while i < size:
    nums[i]=nums[i]/amount*100
    i+=1
i=0
print(f"Target percent:{round(100/size,2)}%")
while i < size:
    accuracy=100-abs(nums[i]-100/size)
    print(f"% of {i+1} in {amount}={round(nums[i],2)}. Accuracy={round(accuracy,2)}%")
    list_accuracy.append(accuracy)
    i+=1
av_accuracy=sum(list_accuracy)/size
print(f"Average accuracy={round(av_accuracy,2)}%")