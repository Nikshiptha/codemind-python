
n=int(input( ))
rev=0
temp=n
while(n!=0):
    d=n%10;
    n=n//10
    rev=rev*10+d
if(rev==temp):
    print("True")
else:
    print("False")