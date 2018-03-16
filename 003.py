'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

#solution in which number is constantly divided with its
#factors to remove composite number factors.
n = 600851475143
factors = []
i=2
while n > 1:
    if n % i == 0:
        factors.append(i)
        while n%i == 0:
            n/=i
    i+=1
print (factors[-1])

