def answer(a):
    h = []
    for i in a:
        if i in ['[', '{', '(']:
            h.append(i)
        else:
            if h == [] or h[-1] + i not in ['()', '{}', '[]']:
                return 'no'
            else:
                h.pop()
    if h == []:
        return 'yes'
    return 'no'
print(answer(input()))

