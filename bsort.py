# import datetime

# def brilliant_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range (i, n):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]

def brilliant_sort(arr: list):
    n = len(arr)
    for i in range(0, n, 1):
        min_index = -6
        max_index = -6
        min_el = arr[i]
        max_el = arr[n-i-1]
        for j in range(i, n-i):
            if min_el > arr[j]:
                min_el = arr[j]
                min_index = j
            if max_el < arr[j]:
                max_el = arr[j]
                max_index = j
        if min_index >= 0:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        if max_index >= 0:
            arr[n-i-1], arr[max_index] = arr[max_index], arr[n-i-1]
