import heapq
def get_answer(n, d, v, r, a):
    answerList = {}
    heap = [[0, d]]
    check = [False for _ in range(n + 1)]
    for i in a:
        answerList[i] = 100**10
        heap.append([100 ** 10, i])
    heap.remove([100 ** 10, d])
    i = d
    heapq.heapify(heap)
    answerList[i] = 0
    while i != v and len(heap) != 0:
        i = heap[0][-1]
        heapq.heappop(heap)
        while check[i]:
            i = heap[0][-1]
            heapq.heappop(heap)
        check[i] = True
        for j in a[i]:
            b = j[0]
            c = j[1]
            e = j[-1]
            if b >= answerList[i] and answerList[c] > e:
                answerList[c] = e
                heapq.heappush(heap, [e, c])


    if answerList[v] == 100**10:
        return -1
    return answerList[v]

with open ('input.txt', 'r') as f:
    n = int(f.readline())
    d, v = map(int, f.readline().split())
    r = int(f.readline())
    A = {i + 1: [] for i in range(n)}
    for i in range(r):
        a, b, c, e = map(int, f.readline().split())
        A[a].append([b, c, e])
print(get_answer(n, d, v, r, A))
