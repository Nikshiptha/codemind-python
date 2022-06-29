
n=int(input( ))
c=0
e=0
o=0
while n!=0:
    d=n%10;
    n=n//10;
    c=c+1;
    if d%2==0:
        e=e+1
    else:
        o=o+1
if e==c:
    print("Even")
elif o==c:
    print("Odd")
else:
    print("Mixed")