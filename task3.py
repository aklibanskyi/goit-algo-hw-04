import timeit
import random

# --- Алгоритм 1: Сортування вставками (Insertion Sort) ---
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Алгоритм 2: Сортування злиттям (Merge Sort) ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
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
    return arr

# --- Функція для вимірювання часу ---
def measure_time(sort_function_name, data, number=10):
    # Використовуємо копію даних, щоб сортування відбувалося In-Place незалежно для кожного тесту
    setup_code = f"from __main__ import {sort_function_name}\ndata = {data.copy()}"
    stmt = f"{sort_function_name}(data)"
    # Для вбудованої функції sorted
    if sort_function_name == "sorted":
        stmt = "sorted(data)"
        
    times = timeit.repeat(stmt=stmt, setup=setup_code, repeat=3, number=number)
    return min(times) / number  # Середній час найшвидшої ітерації

def main():
    sizes = [100, 1000, 5000] # Розміри масивів для тестування
    print(f"{'Розмір':<10} | {'Insertion Sort':<18} | {'Merge Sort':<18} | {'Timsort (sorted)':<18}")
    print("-" * 70)

    for size in sizes:
        # Генеруємо випадковий масив чисел
        test_data = [random.randint(0, 10000) for _ in range(size)]
        
        time_insertion = measure_time("insertion_sort", test_data)
        time_merge = measure_time("merge_sort", test_data)
        time_timsort = measure_time("sorted", test_data)
        
        print(f"{size:<10} | {time_insertion:<18.6f} | {time_merge:<18.6f} | {time_timsort:<18.6f}")

    print("\n--- Аналіз на відсортованих даних (найкращий випадок) ---")
    size = 5000
    sorted_data = list(range(size))
    
    time_insertion = measure_time("insertion_sort", sorted_data)
    time_merge = measure_time("merge_sort", sorted_data)
    time_timsort = measure_time("sorted", sorted_data)
    print(f"{'Відсортов.':<10} | {time_insertion:<18.6f} | {time_merge:<18.6f} | {time_timsort:<18.6f}")

if __name__ == "__main__":
    main()
