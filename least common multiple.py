# write in input two numbers like 'a b' and in output you can see least common multiple of two numbers
a, b = map(int, input().split())
i = 1
x = max(a, b)
while 1:
    x = i * x
    if x % min(a, b) == 0:
        print(x)
        break
    i+=1
