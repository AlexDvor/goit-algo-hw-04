import random
import timeit
import copy


#  Алгоритм: Сортування вставками:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Алгоритм: Сортування злиттям:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Вбудоване сортування (Timsort):
def builtin_sort(arr):
    return sorted(arr)


# Функція для вимірювання часу
def measure_time(sort_func, data):
    stmt = lambda: sort_func(copy.deepcopy(data))
    return timeit.timeit(stmt, number=1)


# Створимо випадковий список чисел
size = 10_000
random_data = [random.randint(0, 10000) for _ in range(size)]


time_insertion = measure_time(insertion_sort, random_data)
time_merge = measure_time(merge_sort, random_data)
time_builtin = measure_time(builtin_sort, random_data)

# результати

print(f"Сортування вставками: {time_insertion:.6f} секунд")
print(f"Сортування злиттям:   {time_merge:.6f} секунд")
print(f"Timsort (sorted):     {time_builtin:.6f} секунд")


print("\n🔎 Висновок:")
print("- Вставки повільні, особливо на великих масивах.")
print("- Злиття набагато швидше, бо має складність O(n log n).")
print("- Timsort (вбудований sorted) — найшвидший, бо поєднує злиття та вставки.")
