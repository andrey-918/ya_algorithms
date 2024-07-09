def get_answer(L, x1, v1, x2, v2):
    answer = []
    a1 = -1
    a2 = -1
    a3 = -1
    a4 = -1
    a5 = -1
    a6 = -1
    if v1 != v2:
        a1 = (x2 - x1) / (v1 - v2)
        a3 = ((L + x2 - x1) / (v1 - v2))
        a5 = (L - x2 + x1) / (v2 - v1)

    elif x1 == x2:
        return [0]

    if v1 + v2 != 0:
        a2 = (L - x1 - x2) / (v1 + v2)
        a4 = (- x2 - x1) / (v2 + v1)
        a6 = (2 * L - x2 - x1) / (v2 + v1)

    # print(a1, a2, a3, a4, a5. a6)
    if a1 >= 0:
        answer.append(a1)
    if a2 >= 0:
        answer.append(a2)
    if a3 >= 0:
        answer.append(a3)
    if a4 >= 0:
        answer.append(a4)
    if a5 >= 0:
        answer.append(a5)
    if a6 >= 0:
        answer.append(a6)
    return answer

L, x1, v1, x2, v2 = map(int, input().split())
answer = get_answer(L, x1, v1, x2, v2)
if len(answer) == 0:
    print("NO")
else:
    print("YES")
    output = min(answer)
    output ="{:.10f}".format(output)
    print(output)

