n = int(input())
lengths = list(map(int, input().split()))
length = 0
max_length = 0
for i in lengths:
    length += i
    max_length = max(max_length, i)
length -= max_length
print((max_length - length) if (max_length - length) > 0 else (length + max_length))
