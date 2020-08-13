t=int(input())
while(t>0):
    t-=1
    n=int(input())
    for i in range(n):
        for j in range(n):
            print("W",end="") if (j+i)%2==0 else print("B",end="")
        print()