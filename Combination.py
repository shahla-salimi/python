# this code get two numbers like 'n k' in input and show in output the Combination of two numbers
def comb(n, k):
    ans = 1
    for i in range(n-k+1, n+1):
        ans *= i
    for i in range(1, k+1):
        ans /= i
    return ans
n, k = map(int, input().split())
result = comb(n, k)
print(result)
