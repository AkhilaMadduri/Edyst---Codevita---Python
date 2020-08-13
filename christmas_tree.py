def treefun(d,p):
    if d>days:
        for i in range(days):
            print(" ",end="")
        print("*")
        return
    else:
        treefun(d+1,p+1)
        for j in range(1,d+1):
            for k in range(days-j):
                print(" ",end="")
            for k in range(j):
                print("*",end="")
            print("*",end="")
            for k in range(j):
                print("*",end="")
            print()
           
t=int(input())
while(t>0):
    t-=1
    days=int(input())
    if days<=1:
        print("You cannot generate christmas tree")
    elif days>20:
        print("Tree is no more")
    else:
        parts=days-1
        treefun(2,1)
        for i in range(2):
            for j in range(days):
                print(" ",end="")
            print("*",end="")
            print()