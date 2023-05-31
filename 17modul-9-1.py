class SymbolError(Exception):
    pass


def no_figure(n):
    if n:
        return True
    raise SymbolError("Пустая строка")


def one_figure(n):
    if len(n) == 1:
        raise SymbolError("Введен всего один символ в последовательность")


def qsort(array, left, right):  # функция сортировки по возрастанию
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def find_ind(x, array, left, right):  # функия поиска индекса введенного числа в последовательности
    middle = (right + left) // 2  # находим середину
    if x <= array[0]:  # если число меньше или равно наименьшему числу последовательности
        return 'Введенное число меньше или равно наименьшему числу последовательности.'
    if x >= array[-1]:  # если число больше или равно наибольшему числу последовательности
        return 'Введенное число больше или равно наибольшему числу последовательности.'
    if left > right:  # если левая граница превысила правую,
        return 'Этот элемент отсутствует в списке'

    elif array[middle] == x:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif x < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
        return find_ind(x, array, left, middle - 1)
    else:  # иначе в правой
        return find_ind(x, array, middle + 1, right)


print("Введите последовательность чисел в одну строку через пробел:", end=" ")
try:
    numbers = [float(x) for x in input().split()]
    no_figure(numbers)
    one_figure(numbers)
except SymbolError as e:  # обращение к исключению как к объекту
    print(f"Произошла ошибка: {e}.")
    exit()
except ValueError as e:
    print(f"Произошла ошибка ValueError: {e}.")
    exit()
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}.")

print("Введите число:", end=" ")
try:
    num = float(input())
except ValueError as e:
    print(f"Произошла ошибка ValueError: {e}.")
    exit()
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}.")
    exit()

qsort(numbers, 0, len(numbers) - 1)  # Сортировка введенного списка
p = find_ind(num, numbers, 0, len(numbers))  # Поиск позиции элемента, который меньше введеного числа
if isinstance(p, int):
    if p - 1 >= 0 and numbers[p] != numbers[p-1]:
        print("Номер позиции элемента, который меньше введенного пользователем числа:", p - 1)
else:
    print(p)
