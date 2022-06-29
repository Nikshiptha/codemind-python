t=int(input())
while t:
    s=0
    t=t-1
    n=int(input())
    m=n
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    if(s==m):
        print("True")
    else:
        print("False")