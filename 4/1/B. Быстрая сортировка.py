def partition(a):
    less = []
    more = []
    if len(a) < 2: return a
    x = (min(a) + max(a)) / 2
    if min(a) == max(a): return a
    for i in a:
        if i < x:
            less.append(i)
        else:
            more.append(i)
    less = partition(less)
    more = partition(more)
    return less + more
rubbish = int(input())
print(*partition(list(map(int, input().split()))))
