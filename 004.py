'''
            Largest palindrome product
            Problem 4

            A palindromic number reads the same both ways.
            The largest palindrome made from the product of two 2-digit numbers is
            9009 = 91 × 99.

            Find the largest palindrome made from the
            product of two 3-digit numbers.
            '''

    #trying to generate pallindrome numbers from top and find 
    #if it is divisible by two 3-digit numbers from top (999) and also
    #quotient is a 3 digit number

from time import time
#returns concatinated number from list of numbers (list[] to pallindromeNumber)
def pallindromeNumber(pallindromeNumberList): 
    return sum([data*10**(5 - index) for index,data in enumerate(pallindromeNumberList)])
    #return int(''.join(str(i) for i in pallindromeNumberList))

#check for factors from top (999)
def checkForFactors(number): 
    s = 999
    while s > 99:
        if number % s == 0 and number / s < 1000:
            return 1
        s -= 1
    return 0

#startsHere
t = time()
a,b,c = 9,9,9
while a >= 0:
    b = 9
    while b >= 0:
        c = 9
        while c >= 0:
            number = pallindromeNumber([a,b,c,c,b,a])
            flag = checkForFactors(number)
            c -=1
            if (flag):
                print ('answer =',number, '\ntime =', time() - t)
                exit(0)
        b -= 1
    a -= 1





