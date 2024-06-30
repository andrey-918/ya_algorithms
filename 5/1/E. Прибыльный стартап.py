n, k, d = map(int, input().split())


n *= 10
n += 9
if n % k > 9:
    n = -1
else:
    n -= n % k
    n = str(n) + '0' * (d - 1)
print(n)
