"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def reverse_number(number, reverse_num=''):
    if (number % 10 == 0) & (number // 10 == 0):
        return print(f'Перевернутое число: {reverse_num}')
    else:
        reverse_num = reverse_num + str(number % 10)
    return reverse_number(number // 10, reverse_num)


reverse_number(int(input('Введите число, которое требуется перевернуть: ')))