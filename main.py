import random


def input_string():
    #функция ввода строки
    inp_str = str(input("Введите строку: "))
    return inp_str


# def prime_number():
#     # n = int(input("Введите верхнюю границу диапазона: "))  # ввод границы
#     n = 10000
#     arr = []
#     for i in range(n + 1):  # заполнение массива числами от 0 до n
#         arr.append(i)
#     # print(arr)
#
#     arr[1] = 0  # число 1 не является простым
#
#     i = 2
#     while i ** 2 <= n:  # проверка всех элементов массива от 2 до последнего
#         if arr[i] != 0:  # если элемент массива не равен 0
#             j = i * 2  # следующее число, кратное i
#             while j <= n:  # проверка всех элементов от j до n
#                 arr[j] = 0  # обнуление элемента
#                 j += i  # следующее число, кратное i
#         i += 1  # переход к следующему числу
#
#     arr = set(arr)  # преобразование массива в set (set удаляет все повторяющеся элементы)
#     arr.remove(0)  # удаление значения 0 из сета
#     # print(arr)
#     arr = list(arr)
#     index = random.randint(0, len(arr) - 1)
#     num1 = arr[index]
#     print("num 1 =", num1)
#     arr.remove(num1)
#     index = random.randint(0, len(arr) - 1)
#     num2 = arr[index]
#     print("num2 =", num2)
#     arr.remove(num2)
#     return num1, num2


def char_to_code(inp_str):
    #функция перевода символов в код Unicode
    inp_str = list(inp_str)
    list_of_codes = []
    list_of_codes_new = []
    for i in inp_str:
        s = ord(i)
        list_of_codes.append(s)
        # print("s[",i,"]=",s)
    # print(list_of_codes)
    # for i, j in enumerate(list_of_codes):
    #     # n = (i % index) * ((j + i) % index1)
    #     n = i >> index
    #     list_of_codes_new.append(n)
    # print('=',list_of_codes_new)
    return list_of_codes


def codes_to_binary(list_of_codes):
    #функция перевода кодов в двоичный код
    list_of_binaries = []
    for i in list_of_codes:
        # b = str(bin(i))
        bin_code = f'{i:b}'
        list_of_binaries.append(bin_code)
    # print(list_of_binaries)
    for i, j in enumerate(list_of_binaries):
        list_of_binaries[i] = int(list_of_binaries[i])

    return list_of_binaries


def encryption(list_of_binaries):
    s = ''
    for i in list_of_binaries:
        s += str(i)
    # print(s)
    # if len(s) % 2 != 0:
    #     s +='0'
    s = list(s)
    len_list = len(s)
    if len_list % 2 != 0:
        s.append('0')
    print("s =", s)
    s1 = s[:int(len_list/2)]
    s2 = s[int(len_list/2):]
    print("s1=", s1, "s2=", s2)
    final_s = ''
    for i, j in zip(s1, s2):
        new_s = i + j
        # print("new_s", new_s)
        final_s += str(int(new_s, 2))
    print("final:", final_s)
st = input_string()
list_of_codes = char_to_code(st)
print(list_of_codes)
list_of_binaries = codes_to_binary(list_of_codes)
print(list_of_binaries)

encryption(list_of_binaries)
