'''
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
from time import time

a = time()
#iterative solution
sum = 0
for i in range(0,1000):
    if i%3==0 or i%5==0:
        sum+=i
print (sum)
#
a = time() - a
print (a)


b = time()
#non iterative solution
n = 1000//3
sum = 3*n*(n+1)/2
n = 999//5
sum += 5*n*(n+1)/2
n = 1000//15
sum -= 15*n*(n+1)/2
print (sum)
#
b = time()- b
print (b)
if a>b:
    print ('b is faster')
else:
    print ('a is faster')