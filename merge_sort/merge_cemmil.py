import time, random, statistics, sys
sys.setrecursionlimit(300000)

def merge(l, r, moves):
    res, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i]); i += 1
        else:
            res.append(r[j]); j += 1
        moves[0] += 1
    while i < len(l):
        res.append(l[i]); i += 1; moves[0] += 1
    while j < len(r):
        res.append(r[j]); j += 1; moves[0] += 1
    return res

def merge_sort(a, moves):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid], moves)
    right = merge_sort(a[mid:], moves)
    return merge(left, right, moves)

random.seed(42)
vector = [random.randint(1, 1_000_000) for _ in range(100_000)]

times, moves = [], [0]
for _ in range(3):
    moves = [0]
    t0 = time.perf_counter()
    merge_sort(vector[:], moves)
    times.append(round(time.perf_counter() - t0, 6))

print(f"Exec 1: {times[0]}s")
print(f"Exec 2: {times[1]}s")
print(f"Exec 3: {times[2]}s")
print(f"Média:  {round(statistics.mean(times), 6)}s")
print(f"DesvPad:{round(statistics.stdev(times), 6)}s")
print(f"Movimentações: {moves[0]:,}")