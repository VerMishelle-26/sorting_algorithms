import time
import random
import matplotlib.pyplot as plt


# === К1: Сортировка пузырьком ===
def bubble_sort(arr):
    """Сортировка пузырьком. O(n²)."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# === К2: Сортировка выбором ===
def selection_sort(arr):
    """Сортировка выбором. O(n²)."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# === К3: Сортировка вставками (для сравнения) ===
def insertion_sort(arr):
    """Сортировка вставками. O(n²)."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# === Проверка алгоритмов ===
print("=== Проверка алгоритмов ===")
test_arr = [64, 25, 12, 22, 11]
print(f"Исходный: {test_arr}")
print(f"Пузырьком:  {bubble_sort(test_arr)}")
print(f"Выбором:    {selection_sort(test_arr)}")
print(f"Вставками:  {insertion_sort(test_arr)}")


# === Сравнение скоростей ===
print("\n=== Сравнение скоростей ===")
sizes = [100, 500, 1000, 2000, 5000]
bubble_times = []
selection_times = []
insertion_times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]

    start = time.perf_counter()
    bubble_sort(arr)
    bubble_times.append(time.perf_counter() - start)

    start = time.perf_counter()
    selection_sort(arr)
    selection_times.append(time.perf_counter() - start)

    start = time.perf_counter()
    insertion_sort(arr)
    insertion_times.append(time.perf_counter() - start)

    print(f"Размер: {size:>5} | Пузырёк: {bubble_times[-1]:.4f} сек "
          f"| Выбор: {selection_times[-1]:.4f} сек "
          f"| Вставки: {insertion_times[-1]:.4f} сек")


# === График ===
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, marker="o", label="Пузырьком O(n²)", color="red")
plt.plot(sizes, selection_times, marker="s", label="Выбором O(n²)", color="blue")
plt.plot(sizes, insertion_times, marker="^", label="Вставками O(n²)", color="green")
plt.title("Сравнение алгоритмов сортировки")
plt.xlabel("Размер списка (n)")
plt.ylabel("Время выполнения (сек)")
plt.legend()
plt.grid(True)
plt.savefig("sorting_comparison_plot.png")
print("\nГрафик сохранён: sorting_comparison_plot.png")