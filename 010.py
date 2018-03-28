'''
Sum of Primes

Sum of primes upto 2 Million
'''
from time import time

#algo1
#primes by dividing odd numbers with numbers to find prime or not
#'''
t1 = time()

sum = 2
l = 2000000
i = 3
while i<l:
    flag = 0
    for j in range(2, int((i**0.5)+1),1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        sum += i
    i += 2
t1 = time() - t1
print ('Sum of primes upto 2 Million = ', sum,'time = ',t1)

#'''
#algo2
#primes by sieve
t2 = time()
l = 2000000
def primeSieve(limit):
    a = [True]*limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i**2, limit, i):
                a[n] = False

n = list(primeSieve(l))
sum = 0
for i in n:
    sum += i
t2 = time() - t2
print ('Sum of primes upto 2 Million = ', sum,'time = ', t2)

print('algo2 is faster by',t1//t2,'times')
