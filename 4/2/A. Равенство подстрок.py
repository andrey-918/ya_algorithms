s = input()
n = int(input())


for i in range(n):
    L, A, B = map(int, input().split())
    if s[A: A + L] == s[B: B + L]:
        print('yes')
    else:
        print('no')
