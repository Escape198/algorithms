#-------------------------------------------------
# Алгоритм сортировки выбором
#-------------------------------------------------

a = [-3, 5, 0, -8, 1, 10]
N = len(a)   

for i in range(N-1):
    minimum = a[i]            # запоминаем минимальное значение
    minimum_index = i               # запоминаем индекс минимального значения
    for j in range(i+1, N):  # поиск миимального среди оставшихся элементов
        if minimum > a[j]:
            minimum = a[j]
            minimum_index = j

    if minimum_index != i:          # обмен значениями, если был найден минимальный не в i-й позиции
        t = a[i]
        a[i] = a[minimum_index]
        a[minimum_index] = t

print(a)
