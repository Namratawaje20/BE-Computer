import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Multithreaded Merge Sort
import threading

def threaded_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_thread = threading.Thread(target=threaded_merge_sort, args=(left_half,))
        right_thread = threading.Thread(target=threaded_merge_sort, args=(right_half,))

        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()

        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Performance comparison
import random

def performance_comparison():
    arr_size = 100000
    random_array = [random.randint(1, 100000) for _ in range(arr_size)]

    # Timing Merge Sort
    start_time = time.time()
    merge_sort(random_array.copy())
    merge_sort_time = time.time() - start_time

    # Timing Multithreaded Merge Sort
    start_time = time.time()
    threaded_merge_sort(random_array.copy())
    multithreaded_merge_sort_time = time.time() - start_time

    print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
    print(f"Multithreaded Merge Sort Time: {multithreaded_merge_sort_time:.6f} seconds")

# Example usage
performance_comparison()
