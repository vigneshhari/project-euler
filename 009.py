from time import time as t


#straight forward 
'''
t1 = t()
s = 1000
for a in range(0,1000//3): 
    for b in range (a+1,1000//2):
        if a**2 + b**2 == (1000 - (a+b))**2:
            print (a*b*(1000-(a+b)))
            print ('time =', (t() - t1)*10**5)
            exit(0)
            
'''

#this one is like 1000 times faster
t2 = t()
from math import ceil
for n in range(1, int( ceil(( (1000//2)**0.5 -1 )//2) ) ):
    for m in range(n,int(ceil((1000//2)**0.5))):
        if m*(m+n) == 1000//2:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            print (a+b+c , a , b, c)
            print ('time =', (t() - t2)*10**5)
            exit(0)
#'''