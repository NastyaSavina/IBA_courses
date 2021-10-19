#упражнение2 №1
a=[]
for n in range (100000,1000000,1):
    k=str(n)
    y=int(k[0])+int(k[1])+int(k[2])+int(k[3])+int(k[4])+int(k[5])
    if y%7==0:
        a.append(int(k))

for i in range (0, len(a)-1, 1):
    if a[i+1]-a[i]==1:
        print("билеты: "+str(a[i+1])+" и "+str(a[i])+" делятся на 7")

