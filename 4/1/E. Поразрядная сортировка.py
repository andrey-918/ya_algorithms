def get_answer(a):
    print('Initial array:')
    z = '**********'
    print(', '.join(a))
    answer = a.copy()

    f = 0
    while f != len(a[0]):
        f += 1
        bucket = {i: [] for i in range(10)}
        print(z)
        print('Phase', f)
        for x in answer:
            bucket[int(x[-f])].append(x)
        answer = []
        for x in bucket:
            if bucket[x] == []:
                print('Bucket ' + str(x) + ': empty')
                continue
            print('Bucket ' + str(x) + ':', ', '.join(bucket[x]))
            for i in bucket[x]:
                answer.append(i)

    print(z)
    print("Sorted array:")
    print(', '.join(answer))


with open('input.txt', 'r') as f:
    a = list(map(str, f.read().split()))

a.pop(0)
get_answer(a)
