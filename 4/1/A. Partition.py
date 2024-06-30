n = int(input())
a = list(map(int, input().split()))
x = int(input())
ans = 0
for i in a:
    if i < x:
        ans += 1
print(ans)
print(n - ans)}
