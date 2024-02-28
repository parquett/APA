import numpy as np
import time
import matplotlib.pyplot as plt


# Define sorting algorithms
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def stalinSort(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= result[-1]:
            result.append(arr[i])
    return result


# Measure execution time
sizes = [100, 500, 1000, 5000, 10000]
times = {'QuickSort': [], 'MergeSort': [], 'HeapSort': [], 'StalinSort': []}

for size in sizes:
    arr = np.random.randint(0, size, size).tolist()  # Convert numpy array to list for compatibility

    start = time.time()
    quickSort(arr.copy())
    times['QuickSort'].append(time.time() - start)

    start = time.time()
    mergeSort(arr.copy())
    times['MergeSort'].append(time.time() - start)

    start = time.time()
    heapSort(arr.copy())
    times['HeapSort'].append(time.time() - start)

    start = time.time()
    stalinSort(arr.copy())
    times['StalinSort'].append(time.time() - start)

# Plotting again
plt.figure(figsize=(10, 6))
for sort, timings in times.items():
    plt.plot(sizes, timings, label=sort)

plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.grid(True)
plt.show()
