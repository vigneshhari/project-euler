'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
 divisible by all of the numbers from 1 to 20?

'''

limit = 21
from time import time

#normal lcm division
'''
a = time()
l = [x for x in range (0,limit)]
i = 2
fac =[]
while i < limit:
    flag = 0
    for j in range(i,limit):
        if l[j] % i == 0:
            flag = 1
            l[j] //= i

    if flag == 0:
        i += 1
    else:
        fac.append(i)
prod = 1
for x in fac:
    prod *= x
a = time() - a
print (prod, a)

#'''
#find primes,
#for all primes within limit,
#lcm = product(largestExponentWithinLimit(prime))
b = time()
primes = [True for i in range(0,limit)]
primes[0], primes[1] = False, False
for index, value in enumerate(primes):
    if index > limit**0.5:
        break
    if value == True:
        for i in range(index**2,limit,index):
            primes[i] = False
primes = {index for index, prime in enumerate(primes) if prime }
lcm = 1
for prime in primes:
    i = 1
    while prime**i < limit:
        i += 1
    lcm *= prime**(i-1)
b = time()- b
print (lcm, b)


#'''




