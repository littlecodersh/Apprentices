p=2
k=2
i=0
b=0
while i<10001:
    if p%k==0:
        if p <= k:
            i+=1
            b=p
        p+=1
        k=2
    else:
        k+=1
print b
