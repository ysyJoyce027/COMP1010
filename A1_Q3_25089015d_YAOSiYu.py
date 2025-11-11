a=0
b=1
templist=[a,b]
N=int(input("enter a positive integer:"))
while N<=0:
    N=int(input("enter a positive integer:"))
if N==1:
    print([0])
elif N==2:
    print([0,1])
else:
    while len(templist)<N:
        num=(int(templist[-2])+int(templist[-1]))
        templist=templist+[num]
    print(templist)