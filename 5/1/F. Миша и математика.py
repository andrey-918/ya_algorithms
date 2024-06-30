def get_answer( numbers ):
    answer = ""
    if sum(numbers) % 2 == 0: #тогда после нечетного надо поставить умножение, что избавит от одного нечетного (3*2 = 6 - остальные тогда дают нечетную сумму, 3*3=9 - остальные тогда дают четную)
        for number in numbers:
            if number % 2 != 0:
                answer += 'x'
                break
            else:
                answer += '+'
    return answer + '+' * (len(numbers) - len(answer) - 1)

n = input()
numbers = list(map(int, input().split()))
print(get_answer(numbers))
