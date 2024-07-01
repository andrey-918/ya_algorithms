import heapq
def get_answer(a, n, s, f):
    answerList = {}
    heap = [[0, s]]
    check = [False for _ in range(n + 1)]

    for i in a:
        answerList[i] = 100**10
        heap.append([100 ** 10, i])
    heap.remove([100 ** 10, s])
    i = s
    heapq.heapify(heap)
    answerList[i] = 0
    while i != f and len(heap) != 0:
        i = heap[0][-1]
        heapq.heappop(heap)
        while check[i] == True:
            i = heap[0][-1]
            heapq.heappop(heap)
        check[i] = True
        for j in a[i]:
            x = j[0]
            y = j[-1]
            h = answerList[i]
            if answerList[x] > y + h:
                answerList[x] = y + h
                heapq.heappush(heap, [y + h, x])


    if answerList[f] == 100**10:
        return -1
    return answerList[f]

with open ('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    A = {i: [] for i in range(n + 1)}
    for i in range(k):
        a, b, g = map(int, f.readline().split())
        A[a].append([b, g])
        A[b].append([a, g])
    s, f = map(int, f.readline().split())

print(get_answer(A, n, s, f))
