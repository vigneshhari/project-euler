n = 1
i = 3
while n < 10001:
    flag = 0
    for j in range(2,int(i**0.5 + 1), 1):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        n += 1
    i += 2
print (i - 2)

