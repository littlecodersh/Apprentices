def sum_fib(number,odd=True):
    a = 0
    b = 1
    L = []
    single=[]
    double=[]
    for i in range(number):
        L.append(b)
        a = b 
        b = a+b
        if b >= number:
        	break
    for each in L:
        if each %2==0:
            double.append(each)
        elif each %2 !=0:
            single.append(each)
    if odd==True:
        return (sum(single)-1)
    else:
        return sum(double)
print (sum_fib(4000000,False))
