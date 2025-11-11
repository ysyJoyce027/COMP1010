x=eval(input("enter a non-negative integer:"))

y=""
if x==0:
    print("the binary is 0")
else:
    while x>0:
        z=x%2
        if z==0:
            y="0"+y
        else:
            y="1"+y
        x=x//2
    print("the binary is:",y)

templist=y
a=0
for i in range(0,len(templist)):
    bit=templist[i]
    c=len(templist)-i-1
    if bit=="0":
        result=0
    else:
        result=2**c
    a=a+result
print("the dec is:",a)
    
b=""
if a==0:
    print("the hex is 0")
else:
    while a>0:
        if 0<=a%16<=9:
            b=str(a%16)+b
        elif a%16==10:
            b="A"+b
        elif a%16==11:
            b="B"+b
        elif a%16==12:
            b="C"+b
        elif a%16==13:
            b="D"+b
        elif a%16==14:
            b="E"+b
        else:
            b="F"+b
        a=a//16
    print("the hex is:",b)

hex_str=b
m=0
for i in range(0,len(b)):
    char=hex_str[i]
    if char=="0":
        num=0
    elif char=="1":
        num=1
    elif char=="2":
        num=2
    elif char=="3":
        num=3
    elif char=="4":
        num=4
    elif char=="5":
        num=5
    elif char=="6":
        num=6
    elif char=="7":
        num=7
    elif char=="8":
        num=8
    elif char=="9":
        num=9
    elif char=="A":
        num=10
    elif char=="B":
        num=11
    elif char=="C":
        num=12
    elif char=="D":
        num=13
    elif char=="E":
        num=14
    else:
        num=15
    d=len(b)-1-i
    result1=num*16**d
    m=m+result1
print("the dec is :",m)