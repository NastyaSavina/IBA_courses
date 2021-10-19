#упражнение3 №10
import random
n=int (input("введите длину списка:\n"))
A=[]
for i in range (n):
    a=random.randint(0,99)
    A.append(a)
print(A)
s=(A[n-1]+A[n-2]+A[n-3])/3
#print(sum(A[-3:])/3)
print(s)

