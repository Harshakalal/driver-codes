import math
def primeFactors(n):
    h=[]
    while n % 2 == 0:
        h.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            h.append(i)
            n = n / i
     
    if n > 2:
        h.append(n)
    co=0
    for i in h:
        if i!=2 and i!=7:
            co=1
    if co==1:
        print("Regular")
    else:
        print("Special")
        
t = int(input())

for i in range(t):
    n = int(input())
    z=(primeFactors(n))
      
