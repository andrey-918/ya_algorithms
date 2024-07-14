def calculate_perimeter(N, cells):
    perimeter = 0
    for r, c in cells:
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            if (nr, nc) not in cells:
                perimeter += 1
    return perimeter

N = int(input())
cells = []
for _ in range(N):
    r, c = map(int, input().split())
    cells.append((r, c))

perimeter = calculate_perimeter(N, cells)
print(perimeter)
