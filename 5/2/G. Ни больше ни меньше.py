def get_answer(mas):
    answer = []
    cur_len = 0
    max_len = 10**5
    for i in mas:
        max_len = min(max_len, i)
        if cur_len + 1 > max_len:
            answer.append(cur_len)
            cur_len = 0
            max_len = i
        cur_len += 1
    if cur_len != 0:
        answer.append(cur_len)
    return answer

t = int(input())
for i in range(t):
    n = int(input())
    mas = []
    mas = list(map(int, input().split()))
    answer = get_answer(mas)
    print(len(answer))
    print(*answer)
