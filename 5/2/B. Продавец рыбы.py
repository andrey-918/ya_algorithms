n, k = map(int, input().split())
days = list(map(int, input().split()))
answer = 0
for i in range(n):
    for j in range (i + 1, min(i + k + 1, n)):
        answer = max(answer, days[j] - days[i])
print(answer)
