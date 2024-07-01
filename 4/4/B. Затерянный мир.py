answer = []
from copy import copy, deepcopy


def ban(mass, _1, _2, n):
    for i in range(n + 1):
        mass[_1][i] = False
        mass[i][_2] = False
        if _1 + i <= n and _2 + i <= n:
            mass[_1 + i][_2 + i] = False
        if _1 - i > 0 and _2 - i > 0:
            mass[_1 - i][_2 - i] = False
        if _1 + i <= n and _2 - i > 0:
            mass[_1 + i][_2 - i] = False
        if _1 - i > 0 and _2 + i <= n:
            mass[_1 - i][_2 + i] = False
    return mass


def get_answer(pos, mass, n):
    if pos >= n:
        for i in range(1, n + 1):
            if mass[pos][i]:
                answer.append(1)
                return
        return
    for i in range(1, n + 1):
        if mass[pos][i]:

            get_answer(pos + 1, ban(deepcopy(mass), pos, i, n) , n)


n = int(input())
mass = [[True for i in range(n + 1)] for j in range(n + 1)]

get_answer(1, mass, n)
print(len(answer))
