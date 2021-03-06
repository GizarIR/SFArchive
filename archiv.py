x = 123456789
print(('3' in str(x)) and ('7' in str(x)))

a = [1,2,3]
print(id(a))

b = a
print(id(b))

print(a is b)

d = [1, 2, 3]
c = [1, 2, 3]
print(c == d) # равны
print (c is d) # но не эквиваенты

x1, x2 = None, None # решение квадратного уравнения
print(x1 is None)
print(x2 is None)

print('Проверяем четность')
z = 2345654 #input('Введите число: ')
print(int(str(z)[0]) % 2 == 0)

#3.3.4
name = 'Арорат' #input("Введите название на этикетке: ")
if name == 'Арорат':
    print("Нашлась подделка!")
else:
    print("Коньяк ", name, "не подделка")

#3.3.5
price = 2500 #int(input('Введите цену кросовок (руб.): '))
cost = 2500
if price <= cost:
    print('Вы можете купить эти кросовки!')
else:
    print('Увы, кросовки слишком дорогие!')

# проверка приведения к bool
x = 2 #input('Enter number: ')
if x:
    x = int(x)
else:
    x = None
print(x is None)

#3.4.1
# Запишите вместо вопросительных знаков выражение, которое вернет True,
# когда каждое из чисел А и В нечетное.

def are_both_odd(A, B):
    return not (A % 2 == 0) and not (B % 2 == 0)

#3.4.2
# Программа должна корректно работать для 1900≤n≤3000.
# Выведите "Високосный" в случае, если год является високосным,
# и "Обычный" — в обратном случае (не забывайте проверять регистр выводимых программой символов).
ny = 2020 #int(input('Введите год для проверки: '))
if 1900 <= ny <= 3000:
    if (ny % 400 == 0) or (ny % 4 == 0 and ny % 100 != 0):
        print('Високосный')
    else:
        print('Обычный')
else:
    print('Год не в проверяемом диапазоне')

hour = 7
if 6 <= hour < 12:
    print('Утро')

#3.4.3
def fun(x, y):
    if x > 0 and y > 0:
        return ("First quarter")
    if x > 0 and y < 0:
        return ("Fourth quarter")
    if y > 0 and x < 0:
        return ("Second quarter")
    if x < 0 and y < 0:
        return ("Third quarter")

if __name__ == "__main__":
    inp1 = -1 #int(input("enter number1 : "))
    inp2 = -1 #int(input("enter number2 : "))
    print(fun(inp1, inp2))

# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"
# В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
def get_wind_class(speed):
    if 1 <= speed <= 4:
        return ('weak [1]')
    elif 5 <= speed <= 10:
        return ('moderate [2]')
    elif 11 <= speed <= 18:
        return ('strong [3]')
    elif speed >= 19:
        return ('hurricane [4]')

print(get_wind_class(3))  # Печатаем результат выполнения

#3.6.5 version1

rec1 = {'_Sym': 'I', '_Val': 1}
rec2 = {'_Sym': 'V', '_Val': 5}
rec3 = {'_Sym': 'X', '_Val': 10}
rec4 = {'_Sym': 'L', '_Val': 50}
rec5 = {'_Sym': 'C', '_Val': 100}
rec6 = {'_Sym': 'D', '_Val': 500}
rec7 = {'_Sym': 'M', '_Val': 1000}

my_lib = [rec1, rec2, rec3, rec4, rec5, rec6, rec7]
print(my_lib[0])
print(my_lib[0]['_Sym'])
print(rec1['_Val'])


num = 20 #int(input('Введите число до 9999: '))
# I можно поставить перед V (5) и X (10), чтобы получить 4 и 9;
# X можно поставить перед L (50) и C (100), чтобы получить 40 и 90;
# C можно поставить перед D (500) и M (1000), чтобы получить 400 и 900.
if num < 4:
    print('I' * num)
elif 4 <= num <= 5:
    print('I' * (5 - num) + 'V')
elif 5 < num < 9:
    print('V' * (num // 5) + 'I' * (num % 5))
elif 9 <= num <= 10:
    print('I' * (10 - num) + 'X') #первый перечень исключений
elif 10 < num < 14:
    print('X' * (num // 10) + 'I' * (num % 10))
elif 14 <= num <= 15:
    print('X' + 'I' * (5 - num % 10) + 'V')
elif 15 < num < 19:
    print('X' + 'V' * (num % 10 // 5) + 'I' * (num % 5))
elif 19 <= num <= 20:
    print('X' + 'I' * (20 - num) + 'X')

#3.6.5 ver2 - good
num = input('Введите число до 3999: ')
x = len(num)

if x == 1:
    num1 = int(num[-1])  # единицы
    num2 = 0  # десятки
    num3 = 0  # сотни
    num4 = 0  # тысячи
elif x == 2:
    num1 = int(num[-1])  # единицы
    num2 = int(num[-2])   # десятки
    num3 = 0  # сотни
    num4 = 0  # тысячи
elif x == 3:
    num1 = int(num[-1]) % 100  # единицы
    num2 = int(num[-2])  # десятки
    num3 = int(num[-3])  # сотни
    num4 = 0  # тысячи
elif x == 4:
    num1 = int(num[-1])  # единицы
    num2 = int(num[-2])# десятки
    num3 = int(num[-3])  # сотни
    num4 = int(num[-4])# тысячи

str1, str2, str3, str4 = '', '', '', ''

if num1 != 0:
    if num1 < 4:
        str1 = 'I' * num1
    elif num1 == 4:
        str1 = 'IV'
    elif 4 < num1 < 9:
        str1 = 'V' + 'I' * (num1 % 5)
    elif num1 == 9:
        str1 = 'IX'

if num2 != 0:
    if num2 < 4:
        str2 = 'X' * num2
    elif num2 == 4:
        str2 = 'XL'
    elif 4 < num2 < 9:
        str2 = 'L' + 'X' * (num2 % 5)
    elif num2 == 9:
        str2 = 'XC'

if num3 != 0:
    if num3 < 4:
        str3 = 'C' * num3
    elif num3 == 4:
        str3 = 'CD'
    elif 4 < num3 < 9:
        str3 = 'D' + 'C' * (num3 % 5)
    elif num3 == 9:
        str3 = 'CM'

if num4 != 0:
    str4 = 'M' * num4

print(str4 + str3 + str2 + str1)

# 3.4.6 Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

u1 = 'user1'

if u1 in user_database:
    print(user_database[u1])
else:
    print('User was not found')

#3.4.6 ver2 - good
# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if username in user_database:
        if user_database[username] == password:
            return True
        else:
            return False
    else:
        return False

# 3.4.7 Запишите условие, которое является истинным,
# когда только одно из чисел А, В и С меньше 45.
# Иногда проще записать все условия и не пытаться упростить их.
# in: fun(1, 46, 46)
# out: 'One of numbers is less than 45'
# in: fun(1, 1, 46)
# out: 'None of numbers is less than 45 or two  numbers are less than 45'


def fun(A, B, C):
    if ((A < 45) and (B >= 45) and (C >= 45)) or\
            ((B < 45) and (A >= 45) and (C >= 45)) or \
            ((C < 45) and (A >= 45) and (B >= 45)):
        return 'One of numbers is less than 45'
    else:
        return 'None of numbers is less than 45 or two or numbers are less than 45'



if __name__ == "__main__":
    A = int(input('Enter first digit\n'))
    B = int(input('Enter second digit\n'))
    C = int(input('Enter third digit\n'))

    print(fun(A, B, C))

# 3.4.8 Запишите логическое выражение, которое определяет, что число А
# не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
# in: fun(-8)
# out: "Number belong to range"
# in: fun(8)
# out: "Number belong to range"
# in: fun(-100)
# out: "Number does not belong to range"
def fun(a):
    return "Number belong to range" if (-10 <= a <= -1) or \
                                       (2 <= a <= 15) else "Number does not belong to range"

if __name__ == "__main__":
    A = int(input('Enter digit\n'))
    print(fun(A))

# 3.4.9 Дано двузначное число. Определите, входит ли в него цифра 5.
# Попробуйте решить задачу с использованием целочисленного деления %
# и деления с остатком //.

def fun(x):
    return True if (x % 10 == 5) or (x // 10 == 5) else False

if __name__ == "__main__":
    n = int(input("Enter digit\n"))
    print(fun(n))

# 3.4.10 Проверьте, все ли элементы в списке являются уникальными.
# (Подсказка: используйте возможности структуры данных set)
def fun(lst):
    return True if len(set(lst)) == len(lst) else False

if __name__ == "__main__":
    n = int(input("enter number of digits"))
    print("enter digits")
    lst = []
    for i in range(n):
        lst.append(int(input()))

    print(fun(lst))

# 3.4.11 Дано натуральное восьмизначное число.
# Выясните, является ли оно палиндромом (читается одинаково
# слева направо и справа налево).
# (Подсказка: использовать целочисленное деление и деление с остатком не нужно.
# Попробуйте преобразовать число к строке, а потом перевернуть эту строку.
# См. материал прошлого модуля).

num = 84322348
my_str = str(num)
my_list = list(my_str)
my_list.reverse()
my_str3 = "".join(my_list)


if my_str == str(my_str3): print(True)
else:
    print(False)
print(my_str)
print(str(my_str3))

# итоговая строчка
# если использовать реверса: "".join(list(str(num).revers())) - то выдается ошибка
# ниже представлен код который переворачивает список и подает на вход join нужный тип данных
print(True if str(num) == "".join(reversed(list(str(num)))) else False)

# итоговое задание по блоку 3 мое решение
print("Что надеть?")

temperature = int(input('Введите температуру на улице в градусах? \n'))

if 20 < temperature < 30:
    isRain = input('Есть осадки? (YES/NO) \n')
    print('Футболку, шорты и дождевик') if isRain == 'YES' else print('Футболку и шорты')
else:
    if not (temperature > 0):
        print('Пуховик')
    else:
        isRain = input('Есть осадки? (YES/NO) \n')
        if isRain == 'NO':
            print('Пальто')
        else:
            if input('Осадки сильные? (YES/NO) \n') == 'YES':
                print('Пальто, резиновые сапоги и зонт')
            else:
                print('Пальто и дождевик')
# Решение итогового задания по модулю правильный ответ 3
# Запрашиваем ввод температуры
temperature = int(input("Input temperature: "))

#для указания начальных статусов дождливости воспользуемся False или None
rainy = None
heavyRain = None

#если температура <0 то про дождь спрашивать бессмысленно
if temperature > 0:
   rainy = input("Is rainy: ") == "yes"
#если идет дождь спросим насколько он серьезный
   if rainy:
       heavyRain = input("Is heavy rain: ") == "yes"


#реализуем логику по схеме
decision = "Не решил что брать. Останусь дома."
if (temperature) > 20 and (temperature < 30) :
   if rainy:
       decision = "Взять футболку шорты и дождевик"
   else:
       decision = "Взять футболку и шорты"
elif temperature > 0:
   if rainy:
       if heavyRain:
           decision = "Взять пальто, резиновые сапоги и зонт"
       else:
           decision = "Взять пальто и дождевик"
   else:
       decision = "Взять пальто"
else:
   decision = "Взять пуховик"


#Выведем наше решение на экран
print(decision)

# 3.6.1 самопроверка Напишите цикл while, который
# находит максимальное натуральное число, квадрат
# которого меньше 1000.

num = 2
q_num = 0

while q_num < 1000:
    q_num = num ** 2
    print('num = ', num)
    print('Квадрат  q_num = ', q_num)
    num += 1

print('Минимальное натуральное число: ', num-2)
print('Его квадрат: ', (num-2) ** 2)

# 3.6.7 Напишите программу, которая считает неотрицательные степени двойки до тех пор,
# пока это число не станет больше 10 000. В ответ запишите количество итераций, которые
# проделывает цикл.

n = 10000
i = 1

while 2 ** i < n:
    i += 1
print(i)

# 3.6.8 Олег положил тысячу рублей в банк под 8 % годовых. Через сколько лет у него
# на счёте будет не менее трёх тысяч рублей? Выведите на экран это число и
# запишите его в ответ.

num = 1000
year = 0

while num < 3000:
    num = num + (num * 0.08)
    year += 1
print('Через ', year, 'лет, будет', round(num, 2), 'рублей')

# ответ из подсказки

money = 1000
year_count = 0
while money < 3000:
    money = money * 1.08
    year_count += 1
print(year_count)

#3.7.2 Попробуйте теперь самостоятельно подсчитать произведение всех чисел от 1 до N включительно.
P = 1  # создаём переменную-счётчик, в которой мы будем считать произведение.
        # подумайте, чему она должна быть равна
N = 5

# запишите цикл for для подсчёта произведения
for i in range(1, N + 1):
    P = P * i

print('Произведения: ', P)

# 3.7.3 печатаем лесенку из звездочек

for i in range(1, 1 + int(input('Введите число: \n'))):
    print('*' * i)

# поиск минимального и максимального значения в матрице
random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Minimal elements:", min_value_rows) # минимальные элементы
print("Their indices:", min_index_rows) # их индексы
print("Maximal elements:", max_value_rows) # максимальные элементы
print("Their indices:", max_index_rows) # их индексы

# 3.8.1 Напишите цикл, который ищет наибольший элемент в матрице.
test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]

for i in test_matrix:
    for j in i:
        print(j, end=" ")
    print()

max_value_matrix = test_matrix[0][0]

for row in test_matrix:
    for index_col in range(len(row)):
        if row[index_col] > max_value_matrix:
            max_value_matrix = row[index_col]

print('Максимальное значение в матрице: ', max_value_matrix)

# 3.8.2 является ли матрица квадратной

test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]

matrix_q = True
col_row = len(test_matrix)

for row in test_matrix:
    if len(row) != col_row:
        matrix_q = False

print(matrix_q)

# Пример с подсчетом букв

text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
text = text.lower() # привели все к нижнему регистру
text = text.replace(" ", "") #убрали пробелы
text = text.replace("\n", "") #убрали символы перевода строки
count = {}  # для подсчета символов и их количества
for letter in text:
   if letter in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[letter] += 1
   else:
       count[letter] = 1

for char, cnt in count.items():
    print(f"Символ {char} встречается {cnt} раз")

# Самопроверка - подсчет слов в строке
text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
#зачистим текст от знаков препинания и больших букв
text = text.lower()
text = text.replace(';', '')
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace(':', '')

#преобразуем текст в список
l_text = text.split()

#создадим словарь для хранения подсчитываемых элементов
count = {}

for word in l_text:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
# распечатаем с подстановкой в строку значений из кортежей получаемых из словаря
for w, col in count.items():
    print(f"""Слово " {w} " встречается в стихотворении {col} раз.""")

# Итоговое задание на циклы - как определить, содержит ли число цифры цифры, 5, 7 или 9
num = int(input('Введите натуральное число \n'))
dig_l = [5, 7, 9]
count = {}

for digit in dig_l:
    num_i = num
    while num_i != 0:
        if num_i % 10 == digit:
            if digit in count:
                count[digit] += 1
            else:
                count[digit] = 1
        num_i //= 10

for d, col in count.items():
    print(f'Цифра {d} в числе {num}  встречается {col} раз')

# 4.2.1 самопроверка

def print_2_add_2():
    print(f'Результат сложения 2 + 2 =  {2+2}')

print_2_add_2()

# 4.2.2 самопроверка

def hello_world():
    print('Hello world!')

hello_world()

# 4.2.3 selftest
def check_divisor(n, a):
    print(f'{a} является ДЕЛИТЕЛЕМ {n}') if n % a == 0 else print(f'{a} НЕ является ДЕЛИТЕЛЕМ {n}')

check_divisor(9, 3)
check_divisor(3, 2)

#4.2.4 selftest

def reverse_stair(n):
    print('version 1')
    for i in range((-1 * n), 0):
        print('*' * (-1 * i))


    print('version 2')
    for i in range(n, 0, -1):
        print('*' * i)

    print('version 3')
    j = n
    while j != 0:
        print('*' * j)
        j -= 1

reverse_stair(5)

#4.2.5 функци которая возвращает количество делителей числа а.

def get_quantity(a):
    q = 0
    for i in range(1, a + 1):
        if a % i == 0:
            q += 1
    return q

num = int(input('Введите число: '))
print(f'Количество делитетелей для числа {num} будет {get_quantity(num)}')

#4.2.5 функци которая возвращает количество делителей числа а.

def get_quantity(a):
    q = 0
    for i in range(1, a + 1):
        if a % i == 0:
            q += 1
    return q

num = 5 #int(input('Введите число: '))
print(f'Количество делитетелей для числа {num} будет {get_quantity(num)}')

def check_palindrom(text):
    #зачистим текст
    text = text.lower()
    text = text.replace(' ', '')
    text = text.replace('\n', '')
    #если по шагам то делаем вот это
    # l_text = list(text)
    # rev_l_text = reversed(l_text)
    # rev_text = "".join(rev_l_text)
    #вариант 1
    if text == "".join(reversed(list(text))):
        return True
    else:
        return False

    #вариант 2
    str = text
    if str == str[::-1]:
        return True
    else:
        return False

print(check_palindrom("Кит на море не романтик"))
print(check_palindrom('test'))

#примеры создание функции, которая создает функции

def get_my_func(num_func):
   def hello_world():
       print("Hello World")

   def hello_gizar():
       print("Hello Gizar")

   if num_func == 1:
       return hello_world
   else:
       return hello_gizar

hello_any_func = get_my_func(1)  # получить функцию в качестве результата

print(type(hello_any_func))  # <class 'function'>
hello_any_func()  # Hello


hello_any_func = get_my_func(2)  # получить функцию в качестве результата

print(type(hello_any_func))  # <class 'function'>
hello_any_func()  # Hello
#пример создание функции, которая создает функции
def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):
        return n * nonlocal_m

    return local_mul

two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
print(two_mul(5))  # 5 * 2
a = two_mul(5)

three_mul = get_mul_func(3)
print(three_mul(5))  # 5 * 2
b = three_mul(5)
c = a + b
print(c)

#4.3.2 функцию, которая будет перемножать любое количество переданных ей аргументов.
def multiplier(*num):
    sum = 1
    for i in num:
        sum *= i
    return sum

print(multiplier(1, 2, 1, 1))

print(multiplier(9, 9, 9, 9, 9))

# Лгически правильно: Не создавать функции с Изменяемыми аргументами (списки и словари)
# а в описании аргументов делать флаг - например None значение и далее внутри функции инициировать переменную
# В примере правильно сделано: установим аргумент name_arg пустым а внутри функции будем проверять его
#
def correct_func(name_arg=None):
   if name_arg is None:
       name_arg = []
   print("Аргумент до изменения", name_arg)
   name_arg.append(1)
   print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[123])
print('-----')
correct_func(name_arg=[456])

# 4.3.3
# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
def sum_n(n):
    if n == 1:
        print(n)
        return 1
    print(n)
    return n + sum_n(n - 1)


print(sum_n(100))

# Задание 4.3.4
# С помощью рекурсивной функции развернуть строку.
# вариант 1
def rev_str(my_str):
    if len(my_str) == 1:
        return my_str
    n = len(my_str) - 1
    return my_str[n] + rev_str(my_str[:n])

print(rev_str('gizar'))

# вариант 2
def reverse_str(string):
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])

reverse_str('test')  # tset



# Задание 4.3.5
# Дано натуральное число N. Вычислите сумму его цифр.
# вариант 1
def sum_n(n):
    if n == 0:
        return n
    return (n % 10) + sum_n(n // 10)

print(sum_n(123))

# вариант 2
def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

print(sum_digit(123))  # 6

# 4.4.1 version 1
# возвращающую бесконечную последовательность натуральных чисел.
def nat(n=1):
   a = 1
   yield a

   while True:
      a += n
      yield a

for num in nat(3):
   if num < 100:
      print(num)
   else:
      break

# 4.4.1 version 2
def count(start=1, step=1):
  counter = start
  while True:
      yield counter
      counter += step

# 4.4.2 Создайте генератор, который по переданному списку создаёт последовательность,
# в которой элементы этого списка бесконечно циклично повторяются.
#
# Например, для списка [1, 2, 3] генератор создаст бесконечную последовательность 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, ... .
# Реализуем при помощи строк
def l_chain(my_list):
   my_str = ', '.join(map(str, my_list)) + ', '
   while True:
      yield my_str
      my_str += my_str

for i in l_chain([1, 2, 3]):
   print(i)

#  4.4.2 version 2 Реализуем при помощи списков и их методовю
#  Сначала делаем раздельную копию списка
#  потом удаляем первый элемент и сохраняем его в переменную
#  добавляем значение из переменной в конец того же списка
#  и отправляем значение переменной наружу из функции

def repeat_list(list_):
   list_value = list_.copy()
   while True:
      value = list_value.pop(0)
      list_value.append(value)
      yield value

for i in repeat_list([1, 2, 3]):
   print(i)

# варианты завершения функций генераторов
# вариант 1
def first_gen(input_):
    yield input_
    input_ += 1
    print(input_)

my_first_gen = first_gen(5)

print(next(my_first_gen))# вернет 5 - yield input_

next(my_first_gen) #вернет 6 ка результат input_ += 1 и print(input_)
# вариант 2
def second_gen(input_):
    yield input_
    input_ += 1
    yield input_
    input_ += 1

    return input_

my_second_gen = second_gen(5)

print(next(my_second_gen)) #5
print(next(my_second_gen)) #6
print(next(my_second_gen)) #StopIteration: 7
# вариант 3
def last_gen():
    for i in range(10):
        yield i
        if i == 5:
            raise StopIteration


my_last_gen = last_gen()

for _ in range(10):
    print(next(my_last_gen))
# 1,2,3,4,5 и потом raise StopIteration

# пример про генерацию списка животных
def my_animal_gen():
    yield 'корова'
    print('-------')
    for i in ['кот', 'собака', 'медведь']:
        yield i
    print('-----')
    yield 'кит'

a = my_animal_gen()
print(next(a))

print(next(a))

for j in a:
    print(j)

# генератор фибоначи

def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

for num in fib():
    print(num)
    if num > 10000:
        break

fib_gen = fib()
fib_gen.close() # закрыли генератор

for i in fib_gen: # не напечаталось ни одного элемента
    print(i)
# Фугкции ввозвращающие функции
def twice_func(inside_func):
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    inside_func()


def hello():
    print("Hello")


test = twice_func(hello)
# Hello
# Hello

# пример Замыкания функции
def make_adder(x):
    def adder(n):
        return n + x # здесь используется замыкание  nonlocal переменная
    return adder

new_adder = make_adder(10)

print(new_adder(100)) #110
print(new_adder(5)) #15

# структура функции декоратор
def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, которые будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper

def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я - оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я - оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0

# 4.5.1 Взять декорированные функции, которые
# возвращают время работы основной функции и найти среднее время
# выполнения для 100 выполнений каждой функции
# version 1
import time

def pow_2():
    return 100000000**2

def in_built_pow():
    return pow(100000000, 2)

def decorator_time(a_func_to_decor):
    def wrapper():
        print(f'Запустилась функция {a_func_to_decor}')
        avg_time = 0
        sum_time = 0
        for i in range(100):
            t0 = time.time()
            result = a_func_to_decor()
            td = time.time() - t0
            sum_time += td
        avg_time = sum_time / 100
        print(f'Среднее время выполнения функция {a_func_to_decor} равно: {avg_time:.10f} ')
        return result
    return wrapper


test1 = decorator_time(pow_2)
test1()
test2 = decorator_time(in_built_pow)
test2()
# версия 2
import time

N = 100


def decorator_time(fn):
    def wrapper():
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        return dt
    wrapper.__name__ = fn.__name__ # присваиваем функции обертке имя текущей модеринзируемой функции
    return wrapper


def pow_2():
    return 10000000 ** 2


def in_build_pow():
    return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
    mean_pow_2 += pow_2()
    mean_in_build_pow += in_build_pow()

# __name__ - позволяет получать имя функции (без данного параметра подставится имя обертки)
# также нужно делать переприсвоение имени функции внутри декоратора стр 1107
print(f"Функция {pow_2.__name__} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow.__name__} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")

# 4.5.2 Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.
def my_decorator(fn):
    count = 0
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        nonlocal count
        count += 1
        print(f'Func {fn} was call {count} time')
        return count
    return wrapper

@my_decorator
def my_print(word):
    print(word)

my_print('ура')

my_print('ущу ура')

# 4.5.3 Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
# Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент
# функции, по значению результат работы функции, например, {n: f(n)}.
#
# И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
# То есть словарь можно считать промежуточной памятью на время работы программы, где будут
# храниться ранее вычисленные значения. Исходная функция, которую нужно задекорировать
# имеет следующий вид и выполняет простое умножение на число 123456789.:
#
# def f(n):
#    return n * 123456789
# версия 1

def decorator_mem(fn):
    memory_fun = {}
    def wrapper(n):
        nonlocal memory_fun
        if n in memory_fun:
            result = memory_fun[n]
            print('Взято из памяти')
        else:
            result = fn(n)
            memory_fun[n] = result
            print('Новое вычисление')
        return result
    return wrapper

@decorator_mem
def f(n):
    return n * 123456789

print(f(2))
# Новое вычисление
# 246913578
print(f(3))
# Новое вычисление
# 370370367
print(f(2))
# Взято из памяти
# 246913578

# версия 2
def cache(func):
   cache_dict = {}
   def wrapper(num):
       nonlocal cache_dict
       if num not in cache_dict:
           cache_dict[num] = func(num)
           print(f"Добавление результата в кэш: {cache_dict[num]}")
       else:
           print(f"Возвращение результата из кэша: {cache_dict[num]}")
       print(f"Кэш {cache_dict}")
       return cache_dict[num]
   return wrapper

# 5.2.5 Используя цикл while, найдите первое целое число, которое не кэшируется в памяти.
a = 1
b = 1
while id(a) == id(b):
    a += 1
    b += 1
print(a)
print(id(a))
print(id(b))
# 257

# Задание 5.2.8
# Впишите вместо знаков «?» операцию сравнения идентификаторов списков до и после
# обновления, чтобы программа распечатала True, если они равны, иначе — False.

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(True if list_id_before == list_id_after else False)

 # Задание 5.2.9
# Задание на самопроверку.
# Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.

text = input('Введите текст: \n')

unique = set(text)

print(f'Количество уникальных символов: {len(unique)}')

# Пусть у нас есть множество абонентов (для простоты — фамилии) и множество
# должников, а мы хотим получить множество абонентов, не имеющих долгов.

abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debt = abons.difference(debtors)

print(non_debt)


# Задание 5.2.11

# Найдите ошибку в коде и запишите исправленную строку полностью в форму ответа.
# Представленная ниже программа должна находить множество символов, которые встречаются
# в двух строках одновременно.

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)


# # пусть a и b - переменные, которые мы хотим проверить
# a, b = 0, 0
#
# if a and b:
#     print("Обе переменные истинные")
#     print(a, b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b) # печать значения одной переменной, которая является истинной
# else:
#     # Программа должна выводить «Обе переменные ложные»,
#     # если они являются таковыми. Дополните условный оператор последним блоком.
#     print('Обе переменные ложные')
#     print(a, b)

# 5.3.11 А мы хотим проверить, является ли оно целым, находится ли в определенном промежутке
# (например от 100 до 999 включительно), да еще и делится ли на 2 и 3 одновременно.
# Очень много условий. И такое случается в реальных проектах.
a = int(input('Введите число: \n'))

if (type(a) == int) and (100 <= a <= 999) and (a % 2 == 0) and (a % 3 == 0):
    print(f'Это наше число: {a}')
else:
    print('Это не наше число')

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print(f'Это наше число: {a}')
else:
    print('Это не наше число')

# вариант 2

print(all(a))


# Задание 5.3.11
# Задание на самопроверку.
#
# Напишите программу, которая на вход принимает последовательность целых чисел,
# и возвращает True, если все числа ненулевые, и False, если хотя бы одно число равно 0.
a = list(map(int, input('Введите последовательность чисел: ').split()))

print(all(a))

# Задание 5.3.12
# Задание на самопроверку.
#
# Напишите программу, которая на вход принимает последовательность целых чисел
# и возвращает True, если все числа равны нулю, и False, если найдется хотя бы
# одно ненулевое число. Разрешается использование только логических операторов и функций all([ ]) и any([ ]).

str_ = list(map(int, input('Введите последовательность чисел').split()))

print(not any(str_))


# Задание 5.3.13
# Задание на самопроверку.
#
# При помощи генератора списков создайте таблицу умножения чисел от 1 до 10.

M = [[i * j for j in range(1, 11)] for i in range(1, 11)]

for line in range(0,10):
    print(M[line])


# Задание 5.3.14
# Задание на самопроверку.
#
# Модифицируйте последний пример таким образом,
# чтобы в список сохранялось True, если элемент четный, и False, если элемент нечетный.

# L = [True if int(input('введите число: ')) % 2 == 0 else False for i in range(5)]

# вариант 2

L = [int(input('введите число: ')) % 2 == 0 for i in range(5)]

print(L)

# Задание 5.3.16
# Задание на самопроверку.
#
# Подумайте, как нужно записать логическое выражение, используя all([ ]) и any([ ]) над списком четности, если его
# результат будет истинным тогда и только тогда, когда в списке есть хотя бы один четный и хотя бы один нечетный элемент.

L = [int(input('введите число для списка четности: ')) % 2 == 0 for i in range(5)]

print(L)

print(any(L) and not all(L))

# Задание 5.3.17
# Задание на самопроверку.
#
# Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M.

L = [i for i in range(10)]
M = [i for i in range(10, 0, -1)]

# for a in zip(L,M):
#     print(a)
#
# for a, b in zip(L, M):
#     print("a = ", a, "b= ", b)

N = [a * b for a, b in zip(L, M)]
print(N)

# Задание 5.3.18
# Задание на самопроверку.
#
# Реализуйте программу, которая сжимает последовательность символов. На вход подается последовательность вида:
#
# aaabbccccdaa
# Необходимо вывести строку, где каждая последовательность из одинаковых символов, идущих подряд, заменяется на один символ, и длину этой последовательности (включая последовательности единичной длины). Вывод должен выглядеть так:
#
# a3b2c4d1a2

text = 'aaabbccccdaa'

count = []
last_letter = None
for i in range(len(text) - 1):
#    print(text[i])

    if (text[i] == text[i + 1]) and (i < len(text)) and last_letter != text[i]:
        j = i
        count_j = 0
        while j < len(text) and text[i] == text[j]:
            j += 1
            count_j += 1
        count.append(text[i])
        count.append(str(count_j))
        last_letter = text[i]
    elif text[i] != text[i-1] and text[i] != text[i+1]:
        count.append(text[i])
        count.append(str(1))
        last_letter = text[i]
    else:
        continue

print("".join(count))
# вариант 2
last = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += last + str(count)  # иначе - записываем в результат
        last = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)

#  Функцию, решающую квадратные уравнения. Вспомним сначала матчасть:

# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня
# Пойдем поэтапно.
# Задание 5.4.3
# Напишите функцию D(a, b, c), возвращающую дискриминант квадратного уравнения.

def D(a, b, c):
    return b**2 - 4*a*c

# Задание 5.4.4
# Реализуйте функцию quadratic_solve(a, b, c), возвращающую «Нет вещественных корней»
# в случае отрицательного дискриминанта.
# 5.4.5
# Далее модифицируем функцию таким образом, чтобы при нулевом дискриминанте возвращалось значение единственного корня.
# И последним этапом нам нужно вернуть сразу два значения. Конечный вид функции будет выглядеть так:

def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return "Нет вещественных корней"
    elif D(a, b, c) == 0:
        return -b/(2*a)
    else:
        return (-b - D(a, b, c)**0.5)/(2*a), (-b + D(a, b, c)**0.5)/(2*a)

# a = float(input('Введите число A: '))
# b = float(input('Введите число B: '))
# c = float(input('Введите число C: '))


# L = list(map(float, input('Введите переменные через пробел: ').split())) или
L = [1, 0, -1]

# 5.4.7 ВМЕСТО print(quadratic_solve(L[0], L[1], L[2])) ЛУЧШЕ писать:

print(quadratic_solve(*L))

M = {'a': 1,
     'b': 0,
     'c': -1}
# 5.4.8 а при использовании словаря можно использовать функцию распаковки **

print(quadratic_solve(**M))


# Задание 5.4.9
#
# Напишите рекурсивную функцию, находящую минимальный элемент списка
# без использование циклов и встроенной функции min().
# вариант 1
L = [6, 2, 1, 4]

def my_min(a):
    if len(a) == 1:
        return a[0]
    if a[0] < a[1]:
        c = a.pop(1)
        return my_min(a)
    else:
        c = a.pop(0)
        return my_min(a)

print(my_min(L))

# вариант 2 (использование срезов подаем на один элемент меньше)
def min_list(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

# Задание 5.4.10
# Напишите рекурсивную функцию, которая зеркально разворачивает число.
# Предполагается, что число не содержит нули.

N = 12345  # result 54321

def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(N))

 # Задание 5.4.11
# Сейчас попробуем реализовать функцию equal(N, S), (через  рекурсия)
# проверяющую, совпадает ли сумма цифр числа N с числом S.
# При написании программы следует обратить внимание на то, что,
# если S стала отрицательной, то необходимо сразу вернуть False.
# версия 1 и 2


def equal(N, S):
    if N and S > 0:
        return equal(N // 10, S - N % 10)
    else:
        return True if S == 0 else False

print(equal(123, 6))

def equal_2(N, S):
    return equal(N // 10, S - N % 10) if N and S else True if not S else False

print(equal_2(0, 6))

# версия 3

def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)

# Задание 5.4.13
# Реализуйте функцию-генератор, каждое значение которого — приближение числа e с некоторым числом n.
# Теперь попробуем написать генератор для приближенного вычисления числа e = 2.718. Для нахождения числа,
# удовлетворяющего необходимой точности будем использовать следующий цикл:
#
# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение
# Для вычисления числа e с определенной точностью можно использовать формулу:
#
# e_n = (1 + 1/n)**n
# В этой формуле число n — натуральное (1, 2, 3 и т. д.).

def e():
    n = 1
    while True:
        yield (1 + 1/n)**n
        n += 1

last = 0
for a in e(): # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого - завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение


# Задание 5.4.15
# Реализуйте функцию-декоратор, которая проверяет доступ к функции по username пользователя.
# Все username пользователей хранятся в глобальной области видимости в списке USERS.
# При согласии пользователя на авторизацию ему предлагается ввести username,
# который также хранится в глобальной области видимости. Функция должна использовать два декоратора:
# один для проверки авторизации вообще (реализован выше), второй — для проверки доступа.

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещен")
    return wrapper

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()

# Примеры из теории

L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))


def even(x):
    return x % 2 == 0

print(list(filter(even, [-2, -1, 0, 1, -3, 2, -3])))

# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))

# тоже самое но через генератор списков
print([i**2 for i in some_list if i > 0])

# лямбда
# Возвести первые 10 натуральных чисел в квадрат
print(list(map(lambda x: x ** 2, range(1, 11))))  # правильно
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def my_function(x1, x2):  # Обычная функция
   return x2 + x1

lambda x1, x2: x2 + x1  # Анонимная функция

# сортировка словаря при помощи лябда по значению

d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"} #в словаре - пара ключ - значение это кортеж

# Чтобы отсортировать его по ключам нужно сделать так

print(dict(sorted(d.items())))

# сортировка по значению словаря
print(dict(sorted(d.items(), key=lambda x:x[1])))

# Задание 5.5.3
# Предположим у нас есть список с данными о росте и весе людей.
# Задача — отсортировать их по индексу массы тела. Он вычисляется по формуле:
# свой рост в сантиметрах возвести в квадрат, потом массу тела в килограммах разделить на полученную цифру.
#
# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]
# вариант с преобразованием в словарь
data_dict = dict(data)

print(data_dict)

print(dict(sorted(data_dict.items(), key=lambda x: x[1]/x[0]**2)))

# вариант со списком

print(list(sorted(data, key=lambda x: x[1]/x[0]**2)))


# Задание 5.5.4
# найти кортеж с минимальным индексом массы тела

# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

print(list(sorted(data, key=lambda x: x[1]/x[0]**2)))
# вариант 1
print(list(sorted(data, key=lambda x: x[1]/x[0]**2))[0])
# вариант 2
print(min(data, key=lambda x: x[1]/x[0]**2))

# Задание 5.5.5
# 1 point possible (graded)
# Замените знаки «???» корректным выражением. Вывести длину каждого элемента в списке.
#
# (Следует использовать метод map)

a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))

# Задание 5.5.6
# Замените знаки «?» корректным выражением. Переведите все строки из списка в верхний регистр (заглавные буквы).

b = ["это", "маленький", "текст", "обидно"]

# вариант 1
print([x.upper() for x in b])

# вариант 2
print(list(map(str.upper, b)))
#  Игра в "Крестики - Нолики"
#  Правила
#  1. Игрок вводит координаты следующего хода
#  2. Программа "отрисовывает" ход и предлагает сделать ход следующему игроку
#  3. Если один из игроков заполняет линию своим символом по горизонтале, вертикале или диагонале, он "Выигрывает"
#  4. Если ни один игрок не заполняет своим символом прямую линию из 3- х символов, то -  "Ничья"
#  Целевая картинка:
#          0 1 2
#        0 x x 0
#        1 - - 0
#        2 x 0 x

# функция печати игрового поля
def print_matix(pf):
    # создадим полное игровое поле, добавим координаты
    full_pf = []
    for i in range(4):
        if i == 0:
            full_pf.append([' ', '0', '1', '2'])
        else:
            str_ = str(i-1) + "".join(list(map(str, pf[i-1])))  # построим новую строку с координатой
            full_pf.append(list(str_))  # добавим новую строку в полное игровое поле
    for i in range(4):
        print(f"""{" ".join(list(map(str, full_pf[i])))}""")


#  функция проверки вводимых значений координат
def right_enter(str_):
    if str_ is None:
        return False
    if len(str_) != 3:
        print('Координаты хода не соответствуют формату. Строка не из 3-х символов')
        return False
    elif not str_[0].isdigit() or not str_[2].isdigit():
        print('Координаты хода не соответствуют формату. Координаты не цифры')
        return False
    elif all([(0 <= int(str_[0]) <= 2),
              (str_[1] == ' '),
              (0 <= int(str_[2]) <= 2)]):
        return True
    else:
        print('Координаты хода не соответствуют формату. Формат ввода: Цифра Пробел Цифра. Цифра от 0 до 2')
        return False


#  функция определения - а не кончилась ли игра? вход - игровое поле и текущий игрок
def end_game(field_game, cur_p):
    sum_count = [0, 0, 0, 0, 0, 0, 0, 0]   # для хранения сумм по строкам (0-2) колонкам (3-5) и диагоналям (6-7)

    # преобразуем игровое поле в числовую таблицу
    dig_matrix = []
    for i in range(3):
        dig_matrix.append([0 if x == '0' else 1 if x == 'x' else 4 for x in field_game[i]])

    # посчитаем значения по строкам, столбцам и диагоналям и сохраним в список сумм
    for i in range(3):
        for j in range(3):
            sum_count[i] += dig_matrix[i][j]
            sum_count[j+3] += dig_matrix[i][j]
            if i == j:
                sum_count[6] += dig_matrix[i][j]
            if (i == j == 1) or (i == 0 and j == 2) or (i == 2 and j == 0):
                sum_count[7] += dig_matrix[i][j]

    # все ходы кончились - ничья
    if all([x < 3 for x in sum_count]):
        print(f'Игра окончена. Ничья')
        return True

    if any([x in [0, 3] for x in sum_count]) and cur_p == 'x':  # проверим список сумм на наличие выйгрышей
        if len(list(filter(lambda x: x == 0, sum_count))) == len(list(filter(lambda y: y == 3, sum_count))):
            print(f'Игра окончена. Ничья')
        elif len(list(filter(lambda x: x == 0, sum_count))) > len(list(filter(lambda y: y == 3, sum_count))):
            print(f'Игра окончена. Выиграл игрок "0"')
        elif len(list(filter(lambda x: x == 0, sum_count))) < len(list(filter(lambda y: y == 3, sum_count))):
            print(f'Игра окончена. Выиграл игрок "X"')
        return True

    return False

# Основной скрипт
# создаем поле для игры
play_field = [['-' for j in range(3)] for i in range(3)]
print_matix(play_field)

cur_hod = None
player = 'x'  # текущий игрок

while not end_game(play_field, player):
    while not right_enter(cur_hod):
        cur_hod = input(f'Введите координаты хода игрока "{player.upper()}" через пробел (пример: 1 2): ')

    if play_field[int(cur_hod[0])][int(cur_hod[2])] == '-':
        play_field[int(cur_hod[0])][int(cur_hod[2])] = player
        player = '0' if player == 'x' else 'x'
        print_matix(play_field)
        cur_hod = None
    else:
        print(f'Поле c координатами: {cur_hod} занято.')
        cur_hod = None

# Практика по вебинарам

# Пример ввода многосрочного текста
text = ''

# a = input('Введите текст: ')
# while a != '':
#     text += a
#     a = input('Введите текст: ')
#
# un = set(text)
# print(len(un))


candidates = [
    ("Иван Иванов" , 200),
    ("Сергей Иванов", 500),
    ("Андрей Иванов", 220),
    ("Иван Сергееы", 100)
    ]
beg = 200
end = 400

for name, points in candidates:
    if beg <= points <= end:
        print(name)

# Дан список точек, описанных несколькими координатами. Нужно найти точку с минимальным расстоянием до начала отсчёта

points = [
    (1, 3),
    (2, 10),
    (15, 1),
    (1, 1)
    ]

min(points, key = lambda pair: pair[0]**2 + pair[1]**2)

# Дан список треугольников, описанных 3-мя сторонами.
# Нужно отсортировать список в порядке убывания периметров треугольников"
points = [
    (2, 3, 2),
    (2, 10, 11),
    (15, 13, 12),
    (3, 4, 5)
    ]

points.sort(key = lambda sides: sum(sides)) #если поставить -sum будет по уменьшению сортировка
print(points)


#Найти индекс минимального элемента в списке
# Стандартный вариант
a = [1, 2, -40, 50, 60,-20, 3]
candidate = 0
candidate_index = 0
for i, elem in enumerate(a):
    if elem < candidate:
        candidate = elem
        candidate_index = i
print(candidate_index)
#   Вариант для питона :)

print(min(enumerate(a), key=lambda pair: pair[1]))


def map_decorator(func):
    def wrapper(arg):
        if isinstance(arg, int):
            return func(arg)
        else:
            return list(map(func, sp))

    return wrapper


@map_decorator
def f(a):
    return a ** 5 + 4 * a ** 2 + 10 * a - 3


@map_decorator
def g(a):
    return a ** 2.71 - 10 + 155 ** (a ** 0.5)


sp = [1, 20, 1, 4, 7, 3]
print(f(sp))
print(g(123))

class User:
    pass

peter = User()
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)

peter.email = "peterrobertson@mail.com"
print(peter.email)
print('\n')
# print(julia.email) - выдаст ошибку

class User:
    number_of_fingers = 5
    number_of_eyes = 2

lancelot = User()
print(lancelot.number_of_fingers)

class Product:
    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantuty_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantuty_in_stock > 0 else False

eggs = Product("eggs", "food", 5)
print(eggs.is_available())

class Event:
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.event_type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.event_type = event.get("type")
        self.session_id = event.get("session_id")

events = [
    {
        "timestamp": 1554583508000,
        "type": "itemViewEvent",
        "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1555296337000,
        "type": "itemViewEvent",
        "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
        "timestamp": 1549461608000,
        "type": "itemBuyEvent",
        "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    }
]

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)

class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age

h = Human()
print(h.get_age())
h.set_age(15)
print(h.get_age())

# наследование

import datetime

class Product:
    max_quantity = 100000

    def __init__(self, name, category, quantity_in_stock):
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False

class Food(Product):
    is_critical = True
    need_to_be_refreshed = True
    refresh_frequency = datetime.timedelta(days=1)

eggs = Food(name="eggs", category="food", quantity_in_stock=5)
print(eggs.max_quantity)
print(eggs.is_available())

class Event():
    def __init__(self, timestamp=0, event_type="", session_id=""):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("event_type")
        self.session_id = event_dict.get("session_id")

    def show_description(self):
        print("This is generic event") # Это общее событие

class ItemViewEvent(Event):
    type = "ItemViewEvent"

    def __init__(self, timestamp=0, session_id="", number_of_views=0):
        self.timestamp = timestamp
        self.session_id = session_id
        self.number_of_views = number_of_views

    def show_description(self):
        print("This event means someone has browsed an item") #Это событие означает, что кто-то просматривал элемент

if __name__ == "__main__":
    test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
                                    number_of_views=6)
    test_view_event.show_description()
    print(test_view_event.type)

# задачи на самопроверку модуля c2.1
from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
rect_4 = Rectangle(4, 3)
rect_5 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

circle_1 = Circle(2)
circle_2 = Circle(4)

print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())

print(rect_1 == rect_2)
print(rect_1 == rect_4)
#----------------------

# Задание 2.2.4 вариант 1 мой вариант
class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a**2

    def __str__(self):
        return f'Квадрат со стороной: {self.a}'


# опишем скласс со статистичеким методом
class SquareFactory:
    @staticmethod
    def get_square(a):
        return Square(a)

square_1 = SquareFactory.get_square(4)


print(square_1)

# вариант 2 из теориических материалов скиллфактори

class Square:
    def __init__(self, side):
        self.side = side

class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)


sq1 = SquareFactory.create_square(1)
print(sq1.side)


# декоратор @property позвляет создавать вычисляемые и проверяемые поля (атрибуты) экземпляра класса
class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # хотим создать новое свойство (атрибут - поле класса) через декоратор метода (это свойство вычисляемое,
    # получаем вычисляемый атрибут)
    @property
    def human_age(self):
        return self.age * 7.3

    # getter поля (атрибута класса) _happiness - внутреенее поле, которое не устанавливается через процедуру
    # создания класса
    @property
    def happiness(self):
        return self._happiness

    #setter для поля _happiness с проверкой его допустимого значения
    @happiness.setter
    def happiness(self, value):
        if 0 <= value <= 100:
            self._happiness = value
        else:
            raise ValueError('Должно быть значение от 0 до 100')


jane = Dog("jane", 4)
print(jane.happiness)
jane.happiness = 100
print('Счастье ', jane.happiness)

print('Человеческий возраст ', jane.human_age)

print(jane._happiness)
#
# jane._happiness = 15
#
# print(jane._happiness)

# декоратор методов классов нужен для того чтобы получить возможность запускать метод родительского класса из эземпляра
# класса потомка, при этом понимать из какого типа объекта (экземпляра какого класса в ветке классов)
# был запущен метод родителя
class ParentClass:

    @classmethod
    def method(cls, arg):
        print("%s classmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)

class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)


ParentClass.method(0)
ParentClass.call_original_method()

ChildClass.method(0)
ChildClass.call_original_method()

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_class_method()  # ParentClassclassmethod. 10

# ParentClass classmethod. 0
# ParentClass classmethod. 5
# ChildClass classmethod. 0
# ChildClass classmethod. 6
# ParentClass classmethod. 1
# ParentClass classmethod. 10

#Задание 2.3.4
# Задание на самопроверку.
# Создать вычисляемое свойство для класса Square. Сделайте метод по вычислению площади свойством.
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер. В сеттере добавьте
# проверку условия, что сторона должна быть неотрицательной.
class Square:
    _side = None

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self._side**2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value > 0:
            self._side = value
        else:
            raise ValueError('Сторона квадрта должна быть больше 0')


square_1 = Square()

print(square_1.area)
square_1.side = 5
print(square_1.area)

# Задание 2.4.8
# Задание на самопроверку.
#
# Создать скрипт, который будет в input() принимать строки, и их необходимо будет
# конвертировать в числа, добавить try-except на то, чтобы строки могли быть сконвертированы в числа.
#
# В случае удачного выполнения скрипта написать: «Вы ввели правильное число».
#
# В конце скрипта обязательно написать: «Выход из программы».
#
# ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else.
try:
    a = input('Введите число: ')
    b = int(a)
except ValueError as e:
    print(f'Вы ввели неправильное число: {a}')
    print(e)
else:
    print(f'Вы ввели: {b}')
finally:
    print('Выход из программы')

# Пример полиморфизма
class Player:
    def ask(self):
        pass

    def move(self):
        self.ask()

class User(Player):
    def ask(self):
        print('Печать из User')

class Ai(Player):
    def ask(self):
        print('Печать из Ai')

a_ = User()

b_ = Ai()

a_.ask()
b_.ask()

# Задание 3.2.5
# Задание на самопроверку.
#
# Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.

class NonPositiveDigitalException(ValueError):
    # print('Сторона квадрата должна быть больше нуля')
    pass

class Square:
    def __init__(self, a):
         if a <= 0:
             # self.a = None
             raise NonPositiveDigitalException('Сторона квадрата должна быть больше нуля')

    @classmethod
    def get_name(cls):
        return cls.__name__

    def __repr__(self):
        return f'Square: {self.a}'

square_1 = Square(-1)
# print(square_1.get_name())
# square_1.a = 1
# print(square_1)
# del square_1



class ParentException(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        print(f'Errors: {error}')


class NonPositiveDigitalException(ParentException):
    def __init__(self, message, error):
        super().__init__(message, error)


class Square:
    def __init__(self, a):
        try:
            if a <= 0:
              self.a = None
              raise NonPositiveDigitalException("Какой то message", "какой то error")
        except ParentException as e:
            print(e)

    @classmethod
    def get_name(cls):
        return cls.__name__

    def __repr__(self):
        return f'Square: {self.a}'

square_1 = Square(-1)

from os import *
import math
import time

# Задание 3.3.5
# Поэкспериментируйте с модулем time. Выведите в консоль текущее время, попробуйте вывести следующие данные:
#
# только время;
# только минуты;
# только дату;
# только месяц.

# print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))
# print(getcwd())
#print(os.listdir())

print(time.strftime("%H:%M:%S", time.localtime()))
print(time.strftime("%M", time.localtime()))
print(time.strftime("%x", time.localtime()))
print(time.strftime("%B", time.localtime()))

i = 10
while i > -1:
    print(i)
    time.sleep(1)
    i -= 1
print('Время вышло')
import mylibrary


def main():

    r = int(input('Введите радиус : '))
    a = int(input('Введите сторону a : '))
    b = int(input('Введите сторону b : '))

    if mylibrary.area_circle(r) > mylibrary.area_square(a, b):
        print("Площадь круга больше площади квадрата")
    elif mylibrary.area_circle(r) < mylibrary.area_square(a, b):
        print("Площадь круга меньше площади квадрата")
    else:
        print("площади равны")

if __name__ == "__main__":
    main()

# Задание 3.4.3
# Задание на самопроверку.
#
# Сделайте функцию, которая принимает от пользователя путь и выводит всю информацию
# о содержимом этой папки. Для реализации используйте функцию встроенного модуля os.walk().
# Если путь не указан, то сравнение начинается с текущей директории.

import os
# from os.path import join

def get_folder(path):
    start_path = path if path != "" else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("Текущая директория: ", root)
        print("----------------------")

        if dirs:
            print("Список папок: ", dirs)
        else:
            print("Список папок пуст")
        print("----------------------")

        if files:
            print('Список файлов: ', files)
        else:
            print("Список файлов пуст")
        print("----------------------")

        print("Все пути:")
        for f in files:
            print("Файл:", os.path.join(root, f))

        for d in dirs:
            print('Папка:', os.path.join(root, d))
        print("========================")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = input('Введите путь к каталогу: \n')
    get_folder(path)


# Задание 3.4.4
# Задание на самопроверку.
#
# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.
with open('test.txt', 'r') as f_in:
    with open('output.txt','w') as f_out:
        for line in f_in:
            f_out.writelines(line)

# Задание 3.4.5
# Задание на самопроверку.
#
# Дан файл numbers.txt, компоненты которого являются действительными числами
# (файл создайте самостоятельно и заполните любыми числам, в одной строке одно число).
# Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.

with open('numbers.txt', 'r') as f_num:
    with open('output.txt', 'w') as f_out:
        l_ = list(map(lambda x: int(x.strip()), f_num.readlines()))
        f_out.writelines(str(min(l_) + max(l_)))
        f_out.writelines('\n')

# вариант который бережет память
filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
   min_ = max_ = float(f.readline())  # считали первое число
   for line in f:
       num =  float(line)
       if num > max_:
           max_ = num
       elif num < min_:
           min_ = num

   sum_ = min_ + max_

with open(output, 'w') as f:
   f.write(str(sum_))
   f.write('\n')

# Задание 3.4.6
# Задание на самопроверку.
#
# В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
# Выведите на экран всех учащихся, чья оценка меньше 3 баллов. Cодержание файла:

with open('students.txt', 'r') as f_in:
    for line in f_in:
        if int(line.split()[-1]) < 3:
            print(line, end='')


# Задание 3.4.7
# Задание на самопроверку.
#
# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).
with open('string_in.txt', 'r') as f_in:
    with open('output.txt', 'w') as f_out:
        for line in reversed(f_in.readlines()):
            f_out.writelines(line)


# Задание 3.5.6
# Напишите контекстный менеджер, который умеет безопасно работать с файлами.
#
# В конструктор объекта контекстного менеджера передаются два аргумента: первый — путь к
# файлу, который надо открыть, второй — тип открываемого файла (для записи, для чтения и т. д.).
# При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
# При выходе из контекстного менеджера файл должен закрываться.
# (Эталоном работы можно считать контекстный менеджер open).

class OpenFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.openned_file = None

    def __enter__(self):
        self.openned_file = open(self.path, self.mode)
        return self.openned_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.openned_file.close()

with OpenFile('test.txt', 'a') as f:
    f.writelines('123\n')

# вариант 2 короче
class OpenFile_2:
    def __init__(self, path, type):
        self.file = open(path, type)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



with OpenFile_2('test.txt', 'a') as f:
    f.writelines('567\n')

# 4. В коде задан список А. Выведите сумму элементов списка с индексами, кратными 3.
a = [1, 2, 3, 4, 5, 6, 7]
print(a)

s = sum([elem for i, elem in enumerate(a) if i % 3 == 0])

print(s)

print(sum(a[::3]))
# 5. В коде задан список А. Циклически сдвиньте элементы списка вправо.

first = a.pop(-1)
a.insert(0, first)
print(a)

n = -1 # количество сдвигов если n меньше длины списка
b = a[:n] + a[n:]
print(b)

# 6. В коде задан спиоск А. Найдите второй и тертий минимумы этого списка.
b = a.copy()
print(sorted(set(a))[1], sorted(set(a))[2])
# или
first_min = b.pop(b.index(min(b)))

second_min = min(b)
b.remove(min(b))
print(second_min)

third_min = min(b)
b.remove(min(b))
print(third_min)

# 7. Сначала пользователь вводит число n с клавиатуры. После с новой строки он вводит число в n-ичной системе счисления.
# Нужно вывести это число в десятичной системе.
# sdfdgjsdf в n= 7 меричном исчеслении это k
# k = f*n**0 + d*n**1+ s*n**3...s*n**6 (где ** степень)
# для N < 10
s = "1234567"
n = 7
ans = 0
for i in range(len(s) - 1):
    ans += int(s[-i]) * n ** i

print(ans)

# int может переводить в N ичное число

n = 7
s_ = "1234567"
ans_ = int(s_, 12)


print(ans_)

# 8. В коде задан список А, который состоит из списков. Нужно в переменной В получить список,
# который получается в результате склеивания списков из А.
A = [[1, 2],[3, 4, 5],[6, 7, 8, 9]]
B =[]
for elem in A:
    for i in elem:
        B.append(i)

B = []
for elem in A:
    B.extend(elem)

B = []
for elem in A:
    B += elem

B = []
B = sum(A, [])

print(B)


# 9. В коде задана переменная text с текстом. Нужно подсчитать для этого текста статистику: сколько раз какой символ
# в этом тексте встретился.
# вар 1
text = "Нужно подсчитать для этого текста статистику: сколько раз какой символ в этом тексте встретился."

unique_text = set(text)

for s in unique_text:
    symbol_count = text.count(s)
    print(f'{s} - {symbol_count}')

# вар 2
stat = {}
for s in text:
    if s in stat:
        stat[s] += 1
    else:
        stat[s] = 1

for s, count_s in stat.items():
    print(f'Символ {s} встречается {count_s} раз')

# вар 3
from collections import Counter

stat = Counter(text)
for s, count_s in stat.items():
    print(f'Символ {s} встречается {count_s} раз')





# 10. Пользователь вводит число n. Нужно вывести, является ли число простым.
# Чтобы понять является ли число простым (делиться на 1 и на самою себя) достаточно перебирать делением не все
# числа от 2 до N-1 а достаточно от 2 до SQRT(N) (квадратный корень)
n = 23
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        print(i)
if is_prime:
    print(f"Число {n} - простое")
else:
    print(f"Число {n} - НЕ простое")


#вар 2
n = 23
is_prime = True
div = 2
while div**2 < n:
    if n % div == 0:
        is_prime = False
        print(i)
    div += 1
if is_prime:
    print(f"Число {n} - простое")
else:
    print(f"Число {n} - НЕ простое")


# 11. Пользователь вводит в консоль строку. Удалите в этой строке каждое второе слово.
str_1 = "123 456 123 456"
print(" ".join(str_1.split()[::2]))

# как удалить все знаки пунктуации из предложенияю в модуле string есть объект punctuation,
# который сожержит полный перечень знаков пунктуации (без пробелов). Метод стрип удаляет из строки знаки пунктуации
import string
c = "Строка в котройо есть несколько слов (!) "
words = c.split()
words = [i.strip(string.punctuation) for i in words]
# очистим пустые строки
words = [word for word in words if word]

print(words)



# 12. Пользователь вводит в консоль целое число. Нужно вывести запись этого числа в двоичной системе счисления.
# используем алгоритм деления на 2 (деление для любого типа числа одинаково)
number = 123
ans = ""
while number:
    if number % 2 == 0:
        ans = "0" + ans
    else:
        ans = "1" + ans
    number = number // 2

print(ans)

# вариант 2
number = 123

ans = bin(number)
print(ans)
print(ans[2:])


#Во сколько раз (примерно) возрастет время работы алгоритма сложностью O(n^2) по сравнению с O(n*log(n))
# на входных данных размера n=10000? Ответ округлите до целого. Помните также, что логарифм берется по основанию 2.
import math
n = 10000
x = n**2

y = n * math.log(n, 2)

times_ = x / y

print('%09.2f' % times_)

# Эксперименты с массивами
# Убедимся в том, что python list реализует именно динамическиймассив.
# Для этого мыможем провести временные тесты. Для их реализацииимпортируем модульtimeit.Функция
# с аналогичным названиемtimeitизмеряет время,которое затрачивается назапуск кода. В качестве
# первого аргумента принимаетисследуемый код (в видестроки), а аргументnumber- количество повторений.
# Мы укажем этот аргументравным 100, чтобы функцийtimeitзапустила наш код100 раз. Результат измеренийразделим
# также на 100, чтобы получить среднее времяработы. Напишем функцию,которая будет возвращать результат измерений

import timeit

def elapsed_time(func, size):
    return timeit.timeit(func % size, number=100) / 100

code_append = """
elements = range(%d) # генератор элементов, которые будут вставляться в список - оценка сложности O(1)
array = [] # список, работу которого тестируем - оценка сложности O(1)
for e in elements: # влияет на оценку сложности n раз 
    array.append(e) #  оценка сложности O(1)
    # итоговая оценка сложности O(1)+ O(1) + n*O(1) = O(n)
"""

for s in range(10, 15):
    measure_1 = elapsed_time(code_append, 2 ** s)
    measure_2 = elapsed_time(code_append, 2 ** (s+1))
    ratio = measure_2 / measure_1
    print("[%d]/[%d] -> %5.2f" % (2**(s+1), 2**s, ratio))

# вставка в начало массива
code_append = """
elements = range(%d) # генератор элементов, которые будут вставляться в список - оценка сложности O(1)
array = [] # список, работу которого тестируем - оценка сложности O(1)
for e in elements: # влияет на оценку сложности n раз 
    array.insert(0, e) #  оценка сложности O(n)
    # итоговая оценка сложности O(1)+ O(1) + n*O(n) = O(n*n) или O(n**2) или O(n^2)
"""

for s in range(10, 15):
    measure_1 = elapsed_time(code_append, 2 ** s)
    measure_2 = elapsed_time(code_append, 2 ** (s+1))
    ratio = measure_2 / measure_1
    print("[%d]/[%d] -> %5.2f" % (2**(s+1), 2**s, ratio))


# Проверка закрывающихся скобок при помощи структуры данных стэк

def par_checker(str_):
    stack = []

    for s in str_:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0

print(par_checker("(5+6)*(7+8)/(4+3)"))
# True

# Задание 4.4.5
# Задание на самопроверку.
# Модифицируйте функцию проверки баланса скобок для двух видов скобок: круглых и квадратных.
# Для реализации такого алгоритма может быть полезным создание словаря, в котором закрывающая
# скобка — ключ, открывающая — значение.
# par_dict = {
#     ')':'('
#     ']':'['
# }

def par_checker_mod(str_):
    stack = []
    # par_dict ={}

    for s in str_:
        if s in "([":
            stack.append({')': '('}) if s == "(" else stack.append({']': '['})
        elif s in ")]":
            if len(stack) > 0 and ")" in stack[-1]:
                stack.pop()
            elif len(stack) > 0 and "]" in stack[-1]:
                stack.pop()
            else:
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0

print(par_checker_mod("(5+6)*[7+8(/(4+3)"))

# вариант2
pars = {")": "(", "]": "["}

def par_checker_mod_2(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(par_checker_mod_2("(5+6)*[7+8(/("))


# Создадим класс Queue - нужная нам очередь - пример реализции структуры данных Очередь (FIFO)
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    # !!! Класс далее нужно дополнить методами !!!
    def is_empty(self): #очередь пустая
        # да, если указатели совпадают и в них содержится ноль
        return self.head == self.tail and self.tasks[self.head] == 0


# Задание 4.4.7
# Добавьте в класс Queue метод size, который возвращает текущий размер очереди.
# Учтите, что необходимо рассмотреть несколько случаев: когда очередь пустая, когда очередь
# полная (какому условию соответствует?), а также отдельное внимание стоит обратить на тот
# случай, когда хвост очереди переместился в начало списка (закольцевался).
    def size(self):  # получаем размер очереди
        if self.is_empty():  # если она пуста
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
            return self.max_size  # значит очередь заполнена
        elif self.head > self.tail:  # если хвост очереди сместился в начало списка
            return self.max_size - self.head + self.tail
        else:  # или если хвост стоит правее начала
            return self.tail - self.head

# Задание 4.4.8
# Добавьте в класс Queue метод add, который добавляет задачу в конец очереди.
# Также учтите, что размер массива ограничен и при достижении этого предела,
# необходимо перенести указатель в положение 0. После добавления задачи в очередь,
# она должна вывести уведомление об этом в формате:
    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов
        # для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size

# Задание 4.4.9
# Добавьте в класс Queue метод show, печатающий информацию о приоритетной задаче в формате
#
# "Задача №1 в приоритете"
    def show(self):
        print(f"Задача №  {self.tasks[self.head]} самая приоритетная (первая) в очередеи")

# Задание 4.4.10
# Добавьте в класс Queue метод do, которая печатает в консоль задачу (=выполняет ее) и,
# соответственно, удаляет ее из очереди, присваивая ей значение 0. Формат вывода:
#
# "Задача №1 выполнена"
    def do(self):  # выполняем приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.tasks[self.head] = 0
        # и циклично перемещаем указатель
        self.head = (self.head + 1) % self.max_size

# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

def p(n):
    print(n)
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)

# 5
# 4
# 3
# 2
# 1
# 0
# 1
# 2
# 3
# 4
# 5

# Простой граф
G = {"Адмиралтейская":
         ["Садовая"],
     "Садовая":
         ["Спасская",
          "Сенная площадь",
          "Адмиралтейская",
          "Звенигородская"],
     "Спасская":
         ["Садовая",
          "Сенная площадь",
          "Достоевская"],
     "Сенная площадь":
         ["Садовая",
          "Спасская"],
     "Достоевская":
         ["Владимирская",
          "Спасская"],
     "Владимирская":
         ["Достоевская",
          "Пушкинская"],
     "Звенигородская":
         ["Пушкинская",
          "Садовая"],
     "Пушкинская":
         ["Звенигородская",
          "Владимирская"]
     }

print(G)

# Алгоритм Дейкстры  - поиск кратчайшего пути
G = {
    "Адмиралтейская":
        {"Садовая": 4},
    "Садовая":
        {"Сенная площадь": 4,
        "Спасская": 3,
        "Адмиралтейская": 4,
        "Звенигородская": 5},
    "Сенная площадь":
        {"Садовая": 4,
        "Спасская": 4},
    "Спасская":
        {"Садовая": 3,
        "Сенная площадь": 4,
        "Достоевская": 6},
    "Звенигородская":
        {"Пушкинская": 3,
        "Садовая": 5},
    "Пушкинская":
        {"Звенигородская": 3,
        "Владимирская": 4},
    "Владимирская":
        {"Достоевская": 3,
        "Пушкинская": 4},
    "Достоевская":
        {"Владимирская": 3,
        "Спасская": 6}
}

D = {k : 100 for k in G.keys()}  # расстояния
start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()}  # флаги просмотра вершин

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
        D[v] = min(D[v], D[min_k] + G[min_k][v])  # минимум
    U[min_k] = True  # просмотренную вершину помечаем


# print(min(1, 2))
# print(U)
print(D)

# Алгоритм Дейкстры  - поиск кратчайшего пути и перечень станций этого пути
G = {
    "Адмиралтейская":
        {"Садовая": 4},
    "Садовая":
        {"Сенная площадь": 4,
        "Спасская": 3,
        "Адмиралтейская": 4,
        "Звенигородская": 5},
    "Сенная площадь":
        {"Садовая": 4,
        "Спасская": 4},
    "Спасская":
        {"Садовая": 3,
        "Сенная площадь": 4,
        "Достоевская": 6},
    "Звенигородская":
        {"Пушкинская": 3,
        "Садовая": 5},
    "Пушкинская":
        {"Звенигородская": 3,
        "Владимирская": 4},
    "Владимирская":
        {"Достоевская": 3,
        "Пушкинская": 4},
    "Достоевская":
        {"Владимирская": 3,
        "Спасская": 6}
}

D = {k : 100 for k in G.keys()}  # расстояния
start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()}  # флаги просмотра вершин
P = {k: None for k in G.keys()} # здесь будем хранить вершину-предок с минимальным расстоянием.

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])

    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
         if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
            P[v] = min_k  # и записываем как предок
    U[min_k] = True  # просмотренную вершину помечаем

some_station = 'Достоевская'
pointer = some_station
path = []
while pointer is not None:
    path.append(pointer)
    pointer = P[pointer]

path.reverse()
for v in path:
    print(v)


# Бинарные деревья
# Описываем через классы

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # вставка левого потомка
    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    # вставка правого потомка
    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    #обход дерева в глубину - префиксный способом pre-order
    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    #обход дерева в глубину - постфиксный способом post-order
    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    #обход дерева в глубину - инфиксный подход in-order
    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию


# создаем корень и его потомки /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

print('Поиск в глубину')
print('-----pre - order------')
node_root.pre_order()
print('-------post - order-------')
node_root.post_order()
print('-------in - order-------')
node_root.in_order()

#Поиск в глубину вариант 2 реализация
#      A
#    B   C
#  D   E
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
print('Поиск в глубину DFS')
dfs(visited, graph, 'A')
print('\n')

# Поиск в ширину BFS
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
print("Поиск в ширину BFS")
bfs(visited, graph, 'A')

# Собственные структуры данных - создаем Список

class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()
        R = ''

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    # добавим элемент в начало списка
    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    # добавим элемент в конец списка
    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    # удаляем первый элемент списка
    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

#     удаляем последний элемент списка
    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count



LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)
print(len(LL))


# Линейный поиск
def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

# array = list(map(int, input().split()))
# element = int(input())

array = [1, 3, 5, 6, 8, 3, 5, 32]
element = 3

print(find(array, element))

# подсчет вхождений элементов

def count(array, element):
    count_ = 0
    for a in array:
        if a == element:
            count_ += 1
    return count_

print(count(array, element))


# двоичный поиск

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = 3 #int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 98))

# Двоичное (бинарное)  дерево поиска
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# В переменной queue у нас находится очередь с вершинами для обхода. Начинаем мы обход с корня дерева.
# То есть с вершины, которая находится в переменной self. Поэтому мы её добавляем первой в очереди.
# дальше алгоритм обхода такой:
# * Забираем вершину из очереди.
# * Добавляем в очередь всех потомков этой вершины.
# * Продолжаем обход и снова забираем новую вершину.

    def __str__(self):  # печать с помощью обхода в ширину
        queue = [self]  # создаем очередь
        values = []  # значения в порядке обхода в ширину
        while queue != []:  # пока она не пустая
            last = queue.pop(0) # извлекаем из начала
            if last is not None:  # если не None
                values.append("%d" % last.value)  # добавляем значение
                queue.append(last.left_child) # добавляем левого потомка
                queue.append(last.right_child) # добавляем правого потомка
        return ' '.join(values)

    # поиск по ключу x
    def search(self, x):
        if self.value == x: #если нашли элемент
            return self # возвращаем ссылку на узел
        elif x < self.value: # или, если значение меньше того что мы ищем, продолжаем
            return self.left_child.search(x) # поиск в левом дереве
        elif x > self.value: # иначе в правом
            return self.right_child.search(x)
        else: # если ненашлось возвращаем False
            return False

    # поиск минимума
    def minimum(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.minimum()

    # поиск максимума
    def maximum(self):
        if self.right_child is None:
            return self
        else:
            return self.right_child.maximum()

    # поиск следующего элемента
    def next_value(self):
        current = self
        successor = None
        while current is not None:
            if current.value > x:
                successor = current
                current = current.left_child
            else:
                current = current.right_child
        return successor

    # поиск предыдущего элемента
    def prev_value(self):
        current = self
        successor = None
        while current is not None:
            if current.value < x:
                successor = current
                current = current.right_child
            else:
                current = current.left_child
        return successor

    def insert(self, x):
        if x > self.value: # идем в правое поддерево
            if self.right_child is not None: # если оно существует,
                self.right_child.insert(x) # делаем рекурсивный вызов
            else: # иначе создаем правого потомка
                self.right_child = BinarySearchTree(x)
        else: # иначе в левое поддерево и делаем аналогичные действия
            if self.left_child is not None:
                self.left_child.insert(x)
            else:
                self.left_child = BinarySearchTree(x)
        return self # возвращаем корень

    def delete(self, x): # первым этапом мы должны найти удаляемый узел и его предка
        parent = self
        node = self
        if not self.search(x):
            return self
        while node.value != x:
            parent = node
            if parent.left_child is not None and x < parent.value:
                node = parent.left_child
            elif parent.right_child is not None and x > parent.value:
                node = parent.right_child
        # по завершении в node хранится искомый узел

        # первый случай - если лист
        if node.left_child is None and node.right_child is None:
            if parent.left_child is node:
                parent.left_child = None
            if parent.right_child is node:
                parent.right_child = None
            if parent.value == x:
                # если нет листов и parent==node до сих пор,
                # значит, нужно вернуть None для корректной работы рекурсии
                return None
        # второй случай - имеет одного потомка
        elif node.left_child is None or node.right_child is None:
            if node.left_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.left_child
                elif parent.right_child is node:
                    parent.right_child = node.left_child
            if node.right_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.right_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child
        else:
            # третий случай - имеет двух потомков
            next_ = node.next_value(x).value # ищем следующее значение
            node.value = next_ # меняем на него
            # делаем рекурсивный вызов
            node.right_child = node.right_child.delete(next_)
        return self
# Drive cod
BinSTree_1 = BinarySearchTree(25)
BinSTree_1.insert(10)
BinSTree_1.insert(15)
BinSTree_1.insert(37)
BinSTree_1.insert(30)
BinSTree_1.insert(65)
print(BinSTree_1)


# Алгоритмы сортировки
# Наивная сортировка
import random

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False
count = 0

while not is_sort:
    count += 1
    random.shuffle(array)

    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
print(count)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 285736

# Небольшое отступление
# n!= 1 * … * (n-2) * (n-1) * n,


# Как посчитать факториал
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1) * n

print(fact(100))

import math
print(math.factorial(100))

# Как посчитать количество цифр в натуральном числе
def count_dig(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

print(count_dig(fact(100)))

# Сортировка выбором по возрастанию и по убыванию
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):
    idx_min = i
    for j in range(i+1, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
        count += 1
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(count)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):
    idx_min = i
    for j in range(i+1, len(array)):
        if array[j] > array[idx_min]:
            idx_min = j
        count += 1
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(count)


# Метод сортировки пузырьком
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j],  array[j + 1] = array[j + 1], array[j]

print(array)

# Сортировка вставками
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx - 1] > x:
        array[idx] = array[idx - 1]
        idx -= 1
    array[idx] = x
print(array)

# Сортировка вставками с подсчетом количества сравнений
# Тут надо понимать, что оператор and лениво вычисляет операнды.
# Если первый операнд ложный, то он не будет вычислять второй, потому
# что уже известно, что результат операции and будет ложным.
# Поэтому тут надо разделить выражения, например так:


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
cnt = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0:
        cnt += 1
        if not(array[idx-1] > x):
            break
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x


print(array)
print(cnt)


# Сортировка слиянием

a = [2, 3, 1, 4, 6, 5, 9, 8, 7]


def merge_sort(L):  # «разделяй»
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # «властвуй»
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(a))


# Быстрая сортировка (с )
import random
a = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def qsort(array, left, right):
    # middle = (left + right) // 2

    # p = array[middle]
    p = random.choice(array[left:right +  1])
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

qsort(a, 0, len(a) - 1)
print(a)

# Расчет редакционного расстояния с тестами
import random
import string
import time

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    if m < n:
        return edit_distance(s2, s1)

    previous = list(range(n+1))

    for i, char1 in enumerate(s1, 1):
        current = [i]
        for j, char2 in enumerate(s2, 1):
            current.append(min(current[j-1] + 1,
                                previous[j] + 1,
                                previous[j-1] + (char1 != char2)))
        previous = current

    return previous[n]

def main():
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))

def test(n_iter = 100):
    for i in range(n_iter):
        length = random.randint(0, 64)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        assert edit_distance(s, '') == edit_distance('', s) == len(s)
        assert edit_distance(s, s) == 0
    assert edit_distance('distance', 'editing') == 5
    assert edit_distance('hello', 'mello') == 1

if __name__ == '__main__':
    for i in range(10):
        start = time.time()
        test(1000)
        end = time.time()
        print(end-start)


import requests
import json

пример 1
r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.content)
print(r.status_code)

# пример 2 GET запрос и получение Текста
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)

print(type(texts))

for i in texts:
    print(i[:50], '\n')

пример 3 GET запрос и получение Словаря
r = requests.get('https://api.github.com')
d = json.loads(r.content)
print(type(d))

print(d['following_url'])

Пример 4 POST запрос
r = requests.post('https://httpbin.org/post', data={'key':'value'})
print(r.content)
print(r.status_code)

Пример 5 POST JSON запрос
data = {'key':'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(data))
print(r.content)
print(r.status_code)

# Задание 5.2.3
# Напишите программу, которая отправляет запрос на генерацию случайных текстов
# (используйте этот сервис). Выведите первый из сгенерированных текстов.
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
print(r.content)
print(r.status_code)
texts = json.loads(r.content)
print(type(texts))
print(texts[0][:50], '......')


# Создание Telegram Bot
import telebot

# CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
#                  "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
#                  "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
#                  "migrate_from_chat_id", "pinned_message"]

TOKEN = "pwd"
bot = telebot.TeleBot(TOKEN)


#
# @bot.message_handlers(filters)
# def function_name(message):
#     bot.reply_to(message, "This is message handler")

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.text)
    bot.reply_to(message, f"Привет тебе, {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def handle_photo(message):
    bot.reply_to(message, "Классный МЕМ 😂")


bot.polling(none_stop=True)


import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup

#
# Парсинг сайта
html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python
tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head>,
# который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится
# основная информация о страничке. Её название и инструкции по отображению в браузере.
#
print(title)  # выводим полученный заголовок страницы

# Парсинг файла
# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с
# помощью html-парсера. Сам html - это то, что мы скачали и поместили в папку из браузера.
#
ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент метода findall
# скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
#
# создаём цикл, в котором мы будем выводить название каждого элемента из списка
 for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>.
    #  Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью.
    # (Гиперссылки в html это всегда тэг <a>)
    print(a.text)  # из этого тега забираем текст, это и будет нашим названием

# Задание 5.4.4
# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
html = '''<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>'''

tree = lxml.html.document_fromstring(html)
tag_2 = tree.xpath('/html/body/tag1/tag2/text()')
print(tag_2)

#Задание 5.4.5
# Используя полученные знания, допишите сделанный в начале юнита скрипт
# (где мы доставали заголовки новостей о Python с Python.org) так, чтобы он показывал ещё и дату добавления новости.
#
# Примечание: Для получения атрибутов тега (т. е. его дополнительных параметров) используется метод .get(<имя атрибута>).

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    times = li.find('time')
    print(times.get('datetime')[:19], a.text)


# Парсинг другим способом - библиотека BeautifulSoup
base = 'https://ru.stackoverflow.com' # выносим базовую ссылку в отдельную переменную, она нам потом понадобится

html = requests.get(base).content # с помощью уже знакомой нам библиотеки requests получаем html код странички целиком

soup = BeautifulSoup(html, 'lxml') # создаём объект супа. Первый аргумент в конструкторе - это весь html код.
# Второй аргумент - сама библиотека для парсинга. В нашем случае lxml

div = soup.find('div', id='question-mini-list') # находим с помощью метода find() нужный нам див уточняя id
# ОБРАТИТЕ ВНИМАНИЕ!
# Не смотря на то что нам и вывелся html-код, сам объект, возвращающийся с метода find не является html-кодом 
# (т. е. строкой). Это точно такой же объект BeautifulSoup, только 
# в нём хранится только нужный нам html, который мы искали.

# print(div) # получаем контейнер со списком вопросов

a = div.find_all('a', class_="s-link")  # find_all возвращает список

# print(a) # пишем в консоль, то что нашли
#
# parent =a[0].find_parent() # если хотим посмотреть родителя первого элемента
#
# print(parent)

# теперь напечатаем перечень вопросов и ссылок на них
for _ in a:
    if str(_).find('s-link__muted') == -1:
        print(_.getText(), _.get('href'))
        


# КЭШ и кэширование с помощью RADIS в данном случае используеся облако REDIS.io
# можно установить сервер redis локально

import redis
import json

red = redis.Redis(
    host = 'redis-16053.c274.us-east-1-3.ec2.cloud.redislabs.com',
    port = 16053,
    password = 'pwd'
)

red.set('var1', 'value1')
print(red.get('var1'))
red.delete('var1')
print(red.get('var1'))

dict1 = {'key1': 'value1', 'key2': 'value2'}
print(type(json.dumps(dict1)))
print(json.dumps(dict1))

red.set('dict1', json.dumps(dict1))

converted_dict = json.loads(red.get('dict1'))

print(type(converted_dict))
print(converted_dict)

red.delete('dict1')
print(red.get('dict1'))

# Задание 5.5.4
# Напишите программу, которая будет записывать и кэшировать номера телефонов ваших друзей.
#
# Программа должна уметь воспринимать несколько команд:
#
# записать номер;
# показать номер друга в консоли при вводе имени;
# удалить номер друга по имени.
# Кэширование надо производить с помощью Redis. Ввод и вывод информации должен
# быть реализован через консоль (с помощью функций input() и print()).

import redis
import json

red = redis.Redis(
    host = 'redis-16053.c274.us-east-1-3.ec2.cloud.redislabs.com',
    port = 16053,
    password = 'pwd'
)

cont = 'True'

while cont:
    action = input('Введите что нужно сделать (write / read / delete / stop): \t')
    if action == 'write':
        red.set(input('Введите имя: \n'), input('Введите телефон: \n'))
    elif action == 'read':
        print(red.get(input('Введите имя для поиска: \n')))
    elif action == 'delete':
        red.delete(input('Введите имя для удаления: \n'))
    elif action == 'stop':
        print('До свидания!')
        break
    else:
        continue

# вариант 2
cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break