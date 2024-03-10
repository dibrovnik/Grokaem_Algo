# Алгоритм сортировки выбором. 

# Работает максимально просто: проходимся по списку и находим
# запись с наибольшим(наименьшим) значением -> добавляем ее в новый список -> повторяем n раз.
# Скорость выполения алгоритма: O(n^2)

def find_smallest(arr):
    smallest = arr[0]   # Для хранения наименьшего значения
    smallest_index = 0  # Для хранения индекса наим. значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

my_list = [2, 3, 1, 4]
print(selection_sort(my_list))


