def answer(n1, a, n2, b):
    ans = []
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


n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))
print(*answer(n1, a, n2, b))
