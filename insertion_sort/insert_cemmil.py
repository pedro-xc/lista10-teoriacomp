import time, random, statistics

def insertion_sort(arr):
    a = arr[:]
    swaps = 0
    for i in range(1, len(a)):
        j = i - 1
        while j >= 0 and a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1
            j -= 1
    return a, swaps

random.seed(42)
vector = [random.randint(1, 1_000_000) for _ in range(100_000)]

times, swaps = [], 0
for _ in range(3):
    t0 = time.perf_counter()
    _, swaps = insertion_sort(vector)
    times.append(round(time.perf_counter() - t0, 6))

print(f"Exec 1: {times[0]}s")
print(f"Exec 2: {times[1]}s")
print(f"Exec 3: {times[2]}s")
print(f"Média:  {round(statistics.mean(times), 6)}s")
print(f"DesvPad:{round(statistics.stdev(times), 6)}s")
print(f"Trocas: {swaps:,}")