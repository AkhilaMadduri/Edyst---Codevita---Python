testcases=int(input())
while(testcases>0):
    testcases-=1
    n=int(input())
    a=3
    b=2
    current='00006'
    for i in range(1,n+1):
        for k in range(3*(n-i)):
            print(" ",end="")
        for j in range(i):
            print(current,end=" ")
            a=a+4
            b=b+2
            current=str(a*b).zfill(5)
        print()
