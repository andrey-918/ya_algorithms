def answer(a, b):
    ans = []
    n1 = len(a)
    n2 = len(b)
    i, j = 0, 0
    while i < n1 or j < n2:
        if i >= n1:
            ans.append(b[j])
            j += 1
        elif j >= n2:
            ans.append(a[i])
            i += 1
        else:
            if a[i] < b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1
    return ans


def dooo(a):
    first = []
    second = []
    if len(a) < 2: return a
    for i in range(len(a)):
        if i % 2 == 0:
            first.append(a[i])
        else:
            second.append(a[i])
    return answer(dooo(first), dooo(second))





n1 = int(input())
a = list(map(int, input().split()))
print(*dooo(a))
