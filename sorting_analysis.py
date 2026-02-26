import random
import time

# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# 2. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key


# 4. Generate Array
def generate_array(size):
    random.seed(42)
    return [random.randint(1, size * 10) for _ in range(size)]


# 5. Measure Time
def measure_time(sort_func, arr):
    copy = arr.copy()
    start = time.perf_counter()
    sort_func(copy)
    end = time.perf_counter()
    return (end - start) * 1000


# 6. Main Test
def main():

    sizes = [10000, 25000, 50000]

    for size in sizes:

        arr = generate_array(size)

        bubble_time = measure_time(bubble_sort, arr)
        selection_time = measure_time(selection_sort, arr)
        insertion_time = measure_time(insertion_sort, arr)

        print(f"\nArray Size: {size}")
        print(f"Bubble Sort: {bubble_time:.2f} ms")
        print(f"Selection Sort: {selection_time:.2f} ms")
        print(f"Insertion Sort: {insertion_time:.2f} ms")


# 7. Run program
if __name__ == "__main__":
    main()