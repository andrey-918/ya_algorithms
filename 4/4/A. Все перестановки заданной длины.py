def get_answer(pos, mass, output, n):
    if pos >= n:
        for i in range(1, n + 1):
            if mass[i]:
                print(output + str(i))
                return
    for i in range(1, n + 1):
        if mass[i]:
            mass[i] = False
            get_answer(pos + 1, mass, output + str(i), n)
            mass[i] = True
    return


n = int(input())
get_answer(1, {i: True for i in range(1, n + 1)}, '', n)

