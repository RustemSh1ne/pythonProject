
# 1) В задании нет этого требования, но поскольку некритично, для собственного удобства будем рассматривать
# только целые числа.
# 2) Поскольку задание обязывает воспользоваться рассмотренным в модуле алгоритмом бинарного поиска,
# который, как мы знаем, некорректно работает с повторяющимися значениями - исключим их.

#сортируем пузырьком
def i_sort_it(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# проверяем на отсутствие повторяющихся значений с помощью множества
def elements_are_unique(array):
    setarray = set(array)
    if len(array) == len(setarray):
        return True     # все элементы уникальны
    else:
        return False    # есть одинаковые

def binary_search(array, element, left, right):
    middle = (right + left) // 2  # находим середину
    if array[middle] < element <= array[middle + 1]:  # если введенное число удовлетворяет условию задачи,
        return (middle) # возвращаем этот индекс
    elif element <= array[middle]:  # если введенное число не больше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе (если введенное число больше элемента в середине) в правой
         return binary_search(array, element, middle + 1, right)


print('Привет! Сегодня работаем только с целыми числами!')
try:
    list_of_numbers = list(map(int,input('Введите последовательность неповторяющихся чисел через пробел: ').split()))
except ValueError as error:
    print(error, 'Только целых чисел!')
else:
    if not elements_are_unique(list_of_numbers):
        print('Неповторяющихся!')
    else:
        list_of_numbers = i_sort_it(list_of_numbers)
        print('Отсортированный список: ', list_of_numbers)

        try:
            entered_number = int(input('Введите целое число больше первого и меньше последнего:'))
            if entered_number <= list_of_numbers[0] or entered_number >= list_of_numbers[-1]:
                raise ValueError('Больше первого и меньше последнего!')
        except ValueError as error:
            print(error, 'Только целое число!')
        else:

            position = binary_search(list_of_numbers, entered_number, 0, len(list_of_numbers))
            print('Для введенного числа:', entered_number)
            print('Искомые номер позиции и значение:',position, list_of_numbers[position])



