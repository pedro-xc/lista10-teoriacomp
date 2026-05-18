import time, random, statistics

def bubble_sort(arr):
    a = arr[:]
    n, swaps = len(a), 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, swaps

random.seed(42)
vector = [random.randint(1, 1_000_000) for _ in range(100_000)]

times, swaps = [], 0
for _ in range(3):
    t0 = time.perf_counter()
    _, swaps = bubble_sort(vector)
    times.append(round(time.perf_counter() - t0, 6))

print(f"Exec 1: {times[0]}s")
print(f"Exec 2: {times[1]}s")
print(f"Exec 3: {times[2]}s")
print(f"Média:  {round(statistics.mean(times), 6)}s")
print(f"DesvPad:{round(statistics.stdev(times), 6)}s")
print(f"Trocas: {swaps:,}")