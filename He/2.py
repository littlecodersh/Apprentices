a=1
b=1
c=1
sum=0
while c<=4000000:
    if c%2==0:
        sum=sum+c
    c=a+b
    a=b
    b=c
print (sum)

