# multiplication table from 1 to any number you want(n)
n = int(input('enter yor number: ')) # it is number that you want

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end=' ') # print rows of multiplication table
    print() # go to newline
