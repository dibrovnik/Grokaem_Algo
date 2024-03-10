# Простейший алгоритм бинарного поиска. Скорость выполнения O(logn). 
# Изначально берем полный массив, затем делим его каждый раз попопал, проверяя среднее число на соответствие искомому.

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:   # Значение найдено!
            return mid
        
        if guess < item:    # Предполагаемое число меньше загаданного -> обновляем нижнюю границу
            low = mid + 1
        
        if guess > item:    # Предполагаемое число больше загаданного -> обновляем верхнюю границу
            high = mid - 1
    return None

my_list = [1, 2, 3, 4, 5, 6]

print(binary_search(my_list, 5))