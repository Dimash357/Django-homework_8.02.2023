import random
import time


def sort_bubble(_src: list[int], is_reverse=False) -> list[int]:
    length = len(_src)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if is_reverse:
                if _src[j] < _src[j + 1]:
                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
            else:
                if _src[j] > _src[j + 1]:
                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
    return _src


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 100 + 1)]

    t_start = time.perf_counter()

    print("sorted list: ", sorted(sort_bubble(list1)))
    # 0.0005 (100) | 0.06 (1 000)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 1000 + 1)]

    t_start = time.perf_counter()

    print("sorted list: ", sorted(selection_sort(list1)))
    # 0.0002 (100) | 0.02 (1 000)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 100 + 1)]

    t_start = time.perf_counter()

    print("sorted list: ", sorted(insertion_sort(list1)))
    # 0.0002 (100) | 0.02 (1 000)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 100 + 1)]

    t_start = time.perf_counter()

    print("sorted list: ", sorted(quick_sort(list1)))
    # 0.0001 (100) | 0.005 (1 000)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 100 + 1)]

    t_start = time.perf_counter()

    print("sorted list: ", sorted(merge_sort(list1)))
    # 0.0001 (100) | 0.005 (1 000)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))
