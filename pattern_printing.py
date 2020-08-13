t = int(input())
test=1
while (test<=t):
    print("Case #{}".format(test))
    test+= 1
    n = int(input())
    total = n * (n+1)
    N = n
    l = []
    for i in range(1, total + 1):
        l.append(i)
    i=0
    while(i<N):
        for j in range(i):
            print("**", end="")
        #print(l[:n],"is the first part")
        for k in l[:n]:
            print(k, end="0")
        #print(l[-n:], "is the secondt part")
        for k in l[-n:]:
            print(k, end="0") if k != l[-1] else print(k,end="")
        print()
        i+=1
        del l[:n]
        del l[-n:]
        n = n - 1