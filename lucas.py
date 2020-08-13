a=int(input())
for i in range(a):
    n=int(input())
    a=2
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b,sep=" ")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            luca=a+b
            a=b
            b=luca
            print(luca,end=" ")
    print()