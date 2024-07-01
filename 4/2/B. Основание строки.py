s = input()

answer = ''
buf = ''
len_answer = 0
gg = ''

for i in range(len(s)):
    buf += s[i]
    if len_answer == 0:
        answer = s[0]
        gg = s[0]
        len_answer += 1
        continue
    if buf == answer:
        buf = ''
    elif s[i] != answer[i % len_answer]:
        answer = gg
        len_answer = i
        if s[i] != s[0]:
            answer += s[i]
            len_answer = i + 1

        buf = ''
    gg += s[i]

print(len_answer)
