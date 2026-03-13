import random
import time
import sys

sys.setrecursionlimit(200000)


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


def selection_sort_subarray(arr, l, r):
    for i in range(l, r):
        min_idx = i
        for j in range(i + 1, r + 1):
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


# 4. Quick Sort (Randomized Partitioning)
def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


# 5. Merge Sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_helper(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_helper(arr, l, m)
        merge_sort_helper(arr, m + 1, r)
        merge(arr, l, m, r)


def merge_sort(arr):
    merge_sort_helper(arr, 0, len(arr) - 1)


# 6. Heap Sort
def max_heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


# 7. Hybrid Merge and Selection Sort
def hybrid_merge_sort_helper(arr, l, r, threshold):
    if r - l + 1 <= threshold:
        selection_sort_subarray(arr, l, r)
    elif l < r:
        m = l + (r - l) // 2
        hybrid_merge_sort_helper(arr, l, m, threshold)
        hybrid_merge_sort_helper(arr, m + 1, r, threshold)
        merge(arr, l, m, r)


def hybrid_merge_sort(arr, threshold):
    hybrid_merge_sort_helper(arr, 0, len(arr) - 1, threshold)


# 8. Kth Smallest Element
def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, low, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, high, k)


def kth_smallest(arr, k):
    if 0 < k <= len(arr):
        return quick_select(arr.copy(), 0, len(arr) - 1, k - 1)
    return None


# 9. Generate Array
def generate_array(size):
    random.seed(42)
    return [random.randint(1, size * 10) for _ in range(size)]


# 10. Measure Time
def measure_time(sort_func, arr, *args):
    copy = arr.copy()
    start = time.perf_counter()
    if args:
        sort_func(copy, *args)
    else:
        sort_func(copy)
    end = time.perf_counter()
    return (end - start) * 1000


# 11. Main Execution
def main():
    sizes = [1000, 25000, 50000, 100000]

    for size in sizes:
        arr = generate_array(size)
        print(f"\nArray Size: {size}")

        print(f"Quick Sort: {measure_time(quick_sort, arr):.2f} ms")
        print(f"Merge Sort: {measure_time(merge_sort, arr):.2f} ms")
        print(f"Heap Sort: {measure_time(heap_sort, arr):.2f} ms")
        print(f"Hybrid Sort (Threshold=6): {measure_time(hybrid_merge_sort, arr, 6):.2f} ms")

        print(f"Bubble Sort: {measure_time(bubble_sort, arr):.2f} ms")
        print(f"Selection Sort: {measure_time(selection_sort, arr):.2f} ms")
        print(f"Insertion Sort: {measure_time(insertion_sort, arr):.2f} ms")

    test_arr = [3, 41, 16, 25, 63, 52, 40]
    k = 3
    k_val = kth_smallest(test_arr, k)
    print(f"\nGiven Array: {test_arr}")
    print(f"Output: {k}rd smallest Element is {k_val}.")


if __name__ == "__main__":
    main()