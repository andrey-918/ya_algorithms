answer = []
def get_perm(pos, mass, output, n, a):
    if pos >= n:
        for i in range(1, n + 1):
            if mass[i]:
                x = '1' + output + str(i) + '1'
                ans = 10000000000000000
                if n == 1:
                    answer.append(0)
                    return
                prev = 1
                road = 0
                for i in range(1, n + 1):
                    b = a[prev - 1][int(x[i]) - 1]
                    if b == 0:
                        road = 10000000000000001
                        break
                    road += b
                    if road > ans:
                        break
                    prev = int(x[i])
                ans = min(ans, road)
                answer.append(ans)
                return
    for i in range(2, n + 1):
        if mass[i]:
            mass[i] = False
            get_perm(pos + 1, mass, output + str(i), n, a)
            mass[i] = True
    return

n = int(input())


a = []
for i in range(n):
    a.append(list(map(int, input().split())))

get_perm(1, {i: True for i in range(1, n + 1)}, '', n, a)
ans = min(answer)
if ans == 10000000000000000:
    print(-1)
else:
    print(ans)
