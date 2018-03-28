
product = 0
a = []
file = open('q11.txt','r')
while True:
    line = file.readline()
    if line == '':
        break
    a.append(list(map(int,line.split())))
for i in a:
    print (i)
i,j = 0,0
l = []
p = []
while i<20:
    j = 0
    p = []
    diagonalLeft = 0
    while j<20:
        if j+3<20:
            right = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3]
        if i+3<20:
            down = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j]
        if i+3<20 and j+3<20:
            diagonalRight = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3]
        if i+3<20 and j-3>=0:    
            diagonalLeft = a[i][j] * a[i+1][j-1] * a[i+2][j-2] * a[i+3][j-3]
        temp = max(right, down, diagonalLeft, diagonalRight)
        if temp > product:
            product = temp
        j+=1
    i+=1
print(product)