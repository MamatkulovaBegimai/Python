# # # # # # num = 125
# # # # # # print(num)

# # # # # # print(type(True))

# # # # # first = 'Hello World. I\'m python developer'
# # # # # print(first)

# # # # # second = "Hello World.  I'm python developer.\n Python the best"
# # # # # print(second)

# # # # # third = """Hello World. I'm python developer.
# # # # # Python the best"""
# # # # # print(third)

# # # # name = input("Введите имя: ")
# # # # print("Добро пожалвать", name)

# # # # num1 = int(input("Введите первое число: "))
# # # # num2 = int(input("Введите второе число: "))
# # # # print(num1 - num2)

# # # it = "IT RUN"
# # # print(len(it))

# # # kgz = "Kyrgyzstan"
# # # print(len(kgz))

# # # full = 'Edzen Dzen'
# # # print(full[9])

# # # language = 'Python'
# # #            #012345
# # # print(language[0:6:2])    

# # # name = input("Введите имя: ")
# # # print("Здравствуйте", name.title())

# # # it = "IT-RUN"
# # # print(it.lower())
# # # hello = "hello"
# # # print(hello.upper())


# # num_1 = int(input("Введите первое число: "))
# # num_2 = int(input("Введите второе число: "))
# # if num_1 > num_2:
# #     print("Первое число больше второго")
# # else:
# #     print("Второе число больше второго")   



# # a = int(input())
# # if a % 2 == 0:
# #     print('четное')
# # else:
# #     print('нечетное')


# # number = int(input("Введите число: "))
# # if number == 10:
# #     print("Десять")
# # elif number == 20:
# #     print("Двадцать")
# # elif number == 100:
# #     print("Сто")
# # else: 
# #     print("Если условия не совпали срабатывает else")    


# # num_1 = 500
# # num_2 = 40
# # num_3 = 57
# # if num_1 > num_2 and num_1 > num_3:
# #     print(num_1, "Больше всех")
# # elif num2 >  num_1 and num_2 > num_3:
# #      print(num_2, "Больше всех")
# # else:
# #     print(num_3, "Больше всех")      

# # password = input("Введите пароль: ")
# # confirm_password = input("Подтвердите пароль: ")
# # if password == "2020itrun" and confirm_password == "2020itrun":
# #     print("Welcome")
# # else:
# #     print("Error")    

# # lst = [1, 2, 3, 4]
# # print(lst)
# # my_list = [1, 2, 3, 4, 5]
# # print(my_list)
# # lst = [1, 2.0, True, "Hello", [1, 2, 3,]]
# # print(lst)

# # numbers = ['один', 'двр', 'три', 'четыре', 'пять']
# # print(numbers)
# # print(numbers[3])

# # cars = ["BMW", "MERSEDES", "LEXUS", "LOTUS"]
# # print(cars[::-1])
# # print(cars[1:3])
# # cars.append("Tesla")
# # cars.append("AUDI")
# # cars.insert(0, "AUDI")
# # cars.pop(0)
# # cars.remove("Lexus")

# # contacts = ["Kurmanbek", "Adilet"]
# # find_name = input("Введите имя которую хотите найти: ")
# # if find_name.title() in contacts:
# #     print("Контакт найден")
# # else:     
# #      print("Не нашли")

# # num_1 = int(input("Введите первое число: "))
# # operation = input("+, -, *, /: ")
# # num_2 = int(input("Введите второе число: "))
# # if operation == "+":
# #     print(num_1 + num_2)
# # if operation == "-":
# #     print(num_1 - num_2)    
# # if operation == "*":
# #     print(num_1 * num_2)  
# # if operation == "/":
# #     print(num_1 / num_2)      

# # numbers = [0.1, 10, 1, 3, 5, 100, 500, 30, 40, 1200]
# # print(max(numbers))
# # print(min(numbers))
# # print(sum(numbers))

# # string ="Билим"
# # print(string.find("л"))
# # .
# # all_types = [10, 'Python', 10, 3.14, 'Python', ['I', 'am', 'list']]
# # all_types.remove(3.14)
# # print(all_types) 

# # data = ()
# # print(type(data))

# # data = ("IT RUN",)
# # print(type(data))

# # lst = ["Лето", "Зима", "Осень"]
# # data = tuple(lst)
# # print(data)

# # tup = (1, 2.0, False, "Hello", [1, 10, 2], (10, 30, 50))
# # print(tup)

# # tup_cars = ("BMW", "LEXUS", "LOTUS")
# # tup_cars[2] = "Tesla"
# # tup_cars.append("Hello")
# # print(tup_cars)
# # tup_cars.remove("BMW")
# # print(tup_cars)

# # lst_cars = ["BMW", "LEXUS", "LOTUS"]
# # lst_cars[2] = 'Tesla'
# # print(lst_cars)
# # lst_cars.append("Mersedes")
# # print(lst_cars)
# # lst_cars.remove("BMW")
# # print(lst_cars)

# # it_company = ("Google", "Amazon", "Facebook", "Instagram", "Telegram")
# # print(it_company[1:4:2])
# # print(it_company[::2])
# # print(it_company)
# # lst_it_company = list(it_company)
# # print(lst_it_company)
# # lst_it_company.append("Space X")
# # print(lst_it_company)
# # it_company = tuple(lst_it_company)
# # print(it_company)

# # a, b, c, d = ("Лето", "Зима", "Осень", "Весна")
# # print(c)

# # name = "Egor"
# # age = "30"
# # (name, age) = (age, name)
# # print(name)
# # print(age)

# num1, num2, num3 = 10, 40, 100
# print(num1)

# num1 = "First"
# num2 = "Second"

# num1, num2 = num2, num1
# print(num2)
# print(num1)

# number = 875974
# name = "Dima"
# print("Name " + name + str(number))
# print(f"Name {name} {number}")

# Praktice

# lst = ["one", "two", "three", "four", "five"]
# elem = lst[-2] 
# # lst[0] = "seven"
# # lst[4] = "eight"
# print(elem)

# lst = ["one", "two", "three", "four", "five"]
# for elem in lst:
#     print(elem)

# lst = ["one", "two", "three", "four", "five"]
# lst[1:3] = ["six", "seven"]
# print(lst)

# lst = ["one", "two", "three", "four", "five"]
# lst.insert(3,'seven')
# print(lst)

# lst = ["one", "two", "three", "four", "five"]
# lst.append("six")
# print(lst)

# lst = ["one", "two", "three", "four", "five"]
# lst2 = ['seven', 'eight']
# lst.extend(lst2)
# print(lst)

# lst = ["one", "two", "three", "four", "five"]
# lst.sort()
#  print(lst)

# num = [1, 4, 10, 2, 3, 5]
# num.sort()
# print(num)

# lst = ["one", "two", "three", "four", "five"]
# lst.reverse()
# print(lst)

# lst = ["one", "two", "three", "four", "five"]
# print(lst.index('four'))

# lst = ["one", "two", "three", "four", "five"]
# removed = lst.pop(2)
# print(lst)
# print(removed)

# lst = ["one", "two", "three", "four", "five"]
# lst.remove("two")
# print(lst)

# lst = ["one", "two", "three", "four", "five"]
# del lst[1:3]
# print(lst)

# fruits = ['apple', 'grape', 'peach', 'banana', 'orange']
# if 'apple' in fruits:
#     print('В списке есть элемент apple')

# name = input("Кого хотите найти? ")
# find = ['Бегимай', 'Мээримай', 'Аделя', 'Сыймык']
# if name in find:
#     print("Найден")
# else:
#     print("Не найден")   

# lst = ["one", "two", "three", "four", "five"]   
# num = [1, 2, 4]     
# lst.extend(num)
# print(lst)

# lst = ["one", "two", "three", "four", "five"]   
# num = [1, 2, 4]
# num.clear()
# print(num, lst)

# lst = ["one", "two", "three", "four", "five"]  
# print(lst.index('three'))

# fruits = ['Banana', 'Apple', 'Grape',['Orange', 'Mango']]
# new_fruits = fruits.copy()
# fruits[-1].pop()
# print(fruits)
# print(new_fruits)


# lst = ["one", "two", "three", "four", "five"]   
# delimiter = " "
# output = delimiter.join(lst)
# print(output)

# num1 = 10 
# num2 = 20
# if num1 == 10 or num2 == 10:
#     print("first")
# if num1 ==20 or num2 == 20:
#     print("second") 
# else:
#     print("Error")   
    
# number = int(input("Введите первое число: "))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# Тернарный оператор
# number = int(input("Введите первое число: "))
# res = "Четное" if number % 2 == 0 else "Нечетное"
# print(res)

# # Сокращение тернарного оператора
# number = int(input("Введите первое число: "))
# print("Четное") if number % 2 == 0 else print("Нечетное")

# Тернарный оператор 2
# number = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# res = "Первое число больше" if number > number2 else "Второе число больше"
# print(res)

# num1 = 20000
# num2 = 400
# num3 = 1000
# result = "Первое число" if num1 > num2 and num1 > num3 else "Второе число" if num2 > num1 and num2 > num3 else "Третье"
# print(result)

# data = ('Лето','Осень')
# data = list(data)
# print(data)


# Цикл for 

# Генерация цифр с помощью функции range()

# for i in range(1001): Генерация цифр с помощью функции range()
    # print(i)


# numbers = [1, 2, 45, 66, 90, 77, 21, 100, 102]
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "Четный")
#     else:
#         print(num, "Нечетный")    


# Итерация над кортежом

# numbers = (1, 2, 45, 66, 90, 77, 21, 100, 102)
# for i in numbers:
#     print(i)

# Итерация над строкой

# it = "ITRUN"
# for i in it:
#     print(i)    

# for i in range(0, 10):
#     print(i)
    
# for i in range(1, 101):
#     if i == 50:
#         print("STOP")
#         break
#     print(i)

# numbers = [1, 2, 45, 66, 90, 77, 21, 100, 102]
# for i in numbers:
#     print(i)
#     if i == 100:
#         print("STOP ITERATION")
#         break
   
# num1 = 10
# num2 = 30
# while num1 < num2:
#     print(num1)   
#     num1 += 1
    
# num = 0
# while True:
#     num += 1 
#     print(num)    
#     if num == 10000:
#         break
    
# import time 

# n = 0
# while True:
#     n += 10
#     print(f"Hack {n}%")    
#     time.sleep(2)
#     if n == 100:
#         print("Hacked")
#         break

# import random

# random_num = random.randint(1, 10)
# n = 0
# # while True:
# #     user_num = int(input("Введите число от 1 до 10: "))
# #     if user_num > 0 and user_num <= 10:
# #         n += 1
# #         if n == 3:
# #             print("У вас закончились попытки")
# #             print(f"Случайное число: {random_num}")
# #             break 
# #         elif random_num == user_num:
# #             print("Вы выиграли!")
# #             break
# #     else:
# #             print("Написано же ввести цифры от 1 до 10")

# # while True:
# #     s = input('Введите что-нибудь : ')
# #     if s == 'выход':
# #         break
# #     if len(s) < 3:
# #         print('Слишком мало')
# #         continue
# #     print('Введённая строка достаточной длины')

# # def printMax(a, b):
# #     if a > b:
# #         print(a, 'максимально')
# #     elif a == b:
# #         print(a, 'равно', b)
# #     else:
# #         print(b, 'максимально')
# # printMax()        

# while True:
#     num = (input("Какой самый большой материк? "))
#     n += 1
#     if num.title() == "Евразия":
#         print("Правильно")
#         break
#     elif n == 3:
#         print("У вас не осталось попыток")
#     else:
#         print("Не правильно")    

# while True:
#     num2 = (input("Высота горы Эверест "))
#     n += 1
#     if num == "8848" or "8849":
#         print("Правильно")
#         break
#     elif n == 3:
#         print("У вас не осталось попыток")
#     else:
#         print("Не правильно")            

# try:
#     print(10 + "10")  
# except TypeError:
#     print("Ошибка типа: неподдерживаемые типы операндов для +: 'int' и 'str'")
    
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Деление на ноль")        

# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
# except ValueError:
#     print("Введите число!")    

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Деление на ноль")  
# finally:
#     print("Я все равно сработаю") 

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         operation = input("+, -, *, /: ")
#         num2 = int(input("Введите второе число: "))
#         if operation == "+":
#             print(num1 + num2)
#         elif operation == "-":
#             print(num1 - num2)   
#         elif operation == "*":
#             print(num1 * num2) 
#         elif operation == "/":
#             try:
#                 print(num1 / num2)  
#             except ZeroDivisionError:
#                 print("Деление на ноль")  
#         else:
#             print("Неправильная операция")            
#     except ValueError:  
#         print("Введите число!")   

# student = {'name' : 'Adilet', 'age' : '17'}
# print(student)
# student['age'] = 18
# print(student)
# del student['age']
# print(student)
# print(student.get('age'))
# student.setdefault('key', 'value')
# print(student)
# student['hello'] = 'world'
# print(student)
# student_dct = dict(name = 'Kurmanbek', age =18 )
# print(student_dct)


# car  = {'name' : 'lexus', 'year' : '2022', 'color' : 'black'}
# print(car.keys())
# print(car.values())
# print(car.items())
# for key, value in car.items():
#     print(key, value)

# ab = { 'Swaroop' : 'swaroop@swaroopch.com',
# 'Larry' : 'larry@wall.org',
# 'Matsumoto' : 'matz@ruby-lang.org',
# 'Spammer' : 'spammer@hotmail.com'
# }
# del ab['Spammer']
# print('\nВ адресной книге {0} контактов\n'.format(len(ab)))
# for name, address in ab.items():
#     print('Контакт {0} с адресом {1}'.format(name, address))
    
# ab['Guido'] = 'guido@python.org'
# if 'Guido' in ab:
#     print("\nАдрес Guido:", ab['Guido'])
# print(ab['Larry'])        


# a = [1, 2, 3, 4, 5]
# b = [2, 3, 4, 5, 6]
# c = a + b
# print(set(c))

# names = {'Adilet', 'Kurmanbek', 'Sardor', 'Adilet'}
# print(names)

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(numbers)

# logic = {1, 1.0, True}
# print(logic)

# strange_app = set('Tiktok')
# print(strange_app)

# pangram = {'сьешь же ещё этих мягких французских булок, да выпей чаю'}
# print(pangram)

# cars = ('BMW', 'MERSEDES', 'TESLA', 'AUDI', 'TESLA')
# set_cars = set(cars)
# print(set_cars)

# types = {1, 2.0, False, "1", (10, 20, 30)}
# print(types)

# some_dict = {'key_one' : 'val_one', 'key_two' : 'val_two'}
# some_set = set(some_dict)
# print(some_dict)

# card_suit = ['heart', 'diamond', 'club', 'spade', 'spade']
# suit_set = set(card_suit)
# print(suit_set)

# unbreakable_diamond = ['Jotaro', 'Josuke', 'Koichi']
# golden_wind = ['Jataro', 'Koichi', 'Giorno']
# overlap = set(unbreakable_diamond) & set(golden_wind)
# print(overlap)

# it_company = {'Google', 'Tesla', 'Amazon'}
# it_company.add('Microsoft')
# print(it_company)

# it_company.remove('Google')
# print(it_company)

# it_company.pop()
# print(it_company)

# for i in it_company:
#     print(i)

# it_company = ["Google", "Tesla", "Amazon"]
# it_company.append('Microsoft')
# frzn_it = frozenset(it_company)
# print(frzn_it)
# frzn_it.remove('Google')
# print(frzn_it)

# nums = []
# for num in range(1, 101):
#     nums.append(num)
# print(nums)

# nums = [num for num in range(1, 101)]
# print(nums)

# nums = []
# for i in range(101):
#     if i % 2 == 0:
#         nums.append(i)
# print(nums)        

# nums = [i for i in range(101) if i % 2 == 0]
# print(nums)

# petrol = {
#     'Ai 100' : 60,
#     'Ai 95' : 55,
#     'Ai 92' : 50,
#     'Ai 80' : 40,
#     'DT' : 35
# }
# new_petrol = {}
# for name, price in petrol.items():
#     new_petrol.setdefault(name, price + 15)
# print(new_petrol)   

# new_petrol = {name:price + 15 for name, price in petrol.items()}
# print(new_petrol) 

# from random import randint
# s = 0
# n = int(input())
# for i in range(n):
#     a = randint(1, 10)
#     s+=a
#     print(a,end=' ')
# print()
# print(s)        

# n = int(input())
# s = 0
# for i in range(n):
#     a = int(input())
#     s+=a
#     print('current s:', s)
# print('total',s)
# print('sred arif=',s/n)    

# a = [1, 10, 4, 43, 64, 90]
# a.sort()
# print(a)

# for i in range(4):
#     print('inside',i)
# print('outside',i)

# s = 0
# for i in range(1, 4):
#     s = s + i
# print(s) 
# while True:
#     n = int(input())
#     if n >= 30:
#         print('Дальше нельзя!')
#         break
#     for i in range(n):
#         print('hello')

# a = [1, 10, 4, 43, 64, 90, 3, 54, 32]

# for i in a:
#     print(i, a.index(i))

# n=len(a)
# for i in range(n):
#     print(i, a[i])
#     a[i]+=5
# print(a)    

# a = [1, 10, 1, 43, 43, 90, 3, 3, 32]
# chet = []
# nechet = []
# n = len(a) 
# for i in range(n): 
#     if a[i] % 2 == 0:
#         chet.append(i+1)
#     else:
#         nechet.append(i+1)
# print(chet)
# print(nechet)                  

# a = {1, 2, 3, 2, 3,1 , 2, 2, 4,}
# b = {'hi', 'ha', 'ho', 'hi', 'je'}
# print(b, type(b))
# c = set('abracadabra')
# print(c)
# d = set([1, 2, 3, 2, 1, 3, 4])
# print(d)
# e = set(range(5))
# print(e)
# f = {}
# print(f)
# g = set([[1, 2], [2, 3], [1, 2], [2, 5]])
# print(g)

# a = {4, 3, 2, 1}
# b = {3, 4, 5, 6, 7}
# c = {10, 11, 12}
# # print(a.intersection(b))
# # a.add(9)
# # a.update([5, 6, 7])
# # print(a)
# # a.clear()
# # print(a)

# print(b - a)
# b -= a
# print(b)

# text = input()
# a= set()
# while text !='':
#     slova = text.split()
#     a.update(slova)
#     text = input()
# print(len(a))    

# guess = input()
# passord = 'gwerty'
# count = 0
# while guess != passord:
#     count+=1
#     print('Неправильный ввод пороля')
#     guess = input()
# print('Вы потратили', count, 'попыток')    

# s = 'hsdfdjei348905%$#'
# while len(s) > 0:
#     bukva = s[0]
#     if bukva>='a' and bukva<='z':
#         print(bukva,'small')
#     elif bukva>='A' and bukva<='Z':
#         print(bukva,'big')
#     elif bukva.isdigit():
#         print(bukva, 'digit')
#     else:
#         print(bukva,'znak')
#     s = s[1:]    

# ФУНКИИ
     
# def hello():
#     print('Hello, World')  

# def it():
#     print('IT RUN')

# hello() 
# it()   

# def calc():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(num1 +num2)
# calc()   

# def calc(num1, num2):
#     print(num1 / num2)
# calc(10, 4)    

# def chet_nechet(number):
#     if number % 2 == 0:
#         print(number, 'четный')
#     else:
#         print(number, 'нечетный')    
# chet_nechet(7)      

# def for_range(number):
#     for i in range(1, number):
#         print(i)
# for_range(1001)        

# def mult(num1 = 2, num2 = 3):
#     print(num1 * num2)
# mult()    

# def sayHello():
#     print('hello')
#     print('world')
#     print('and everybody')
# sayHello() 
# print('pause')
# sayHello() 
   
# def square(x, y):
#     print("Квадрат числа ", x, "=", x**2)
# square(4, 5)    

# for i in range(1, 11):
#     square(i)    

# def multiply(a, b):
#     print(a*b)
# multiply(3, 5)    

# def even(a):
#     if a % 2 == 0:
#         print(a, 'chetnoe')
#     else:
#         print(a, 'nechetnoe')
# for i in range(2, 10):
#     even(i)    

# def factorial(n):
#     pr = 1
#     for i in range(2, n+1):
#         pr = pr * i
#     print(pr)  
# factorial(3)               

# if 5 > 10:
#     def primer():
#         print('hello')
# else:
#     def primer():
#         print('Hello')   
# primer()             

# greeting = 'Hello'
# to = 'world'

# def greet(message, name):
#     result = f'{message}, {name}'
#     return result

# g = greet(greeting, to)  
# print(g)

# movie = 'The good, the bad, and the ugly'
# rating = 100
# def result():
#     result = f'Movie: "{movie}", rating: {rating}'
#     print(result)
# result()    

# movie = 'Alien'
# rating = 200
# result()

# movie = 'Вышка'
# rating = 250
# result()

# def welcome(*names):
#     for name in names:
#         print(name, "welcome")
# welcome("Kurmanber", "Sardor", "Adilet", "Begimai")   

# def translate(**words):
#     for key, value in words.items():
#         print(key, value)
# translate(USA = 'США', Russia = 'Россия', Kyrgyztan = 'Кыргызстан')             

# def ochki(name, *args):
#     print(name, args)
# ochki(34, 45, 435)          

# x = ["Виноград", "Манго", "Фрукты", "Клубника"]
# print(set(x))    

# def inc(x):
#     x = x + 1
#     return x 
# lis = [1, 2, 3, 4, 5]
# result = map(inc,lis)
# for x in result:
#     print(x) 

# def cylinder():
#     r = float(input())
#     h = float(input())
#     side = 2 * 3.14 * r * h
#     circle = 3.14 * r ** 2
#     full = side + 2 * circle
#     return side, full
# sCyl, fCyl = cylinder()
# print('Площадь боковой поверхности %.2f' % sCyl)
# print('Полная площадь %.2f' % fCyl)

# def getinput():
#     a = input()
# getinput()    

# def add(num1, num2):
#     print(num1 + num2)    
    
# def sub(num1, num2):
#     print(num1 - num2)
    
# it = 'IT-RUN'

# def students(*names):
#     print(names)
  
# def num():
#     three = []
#     five = []
#     three_five = []
#     for i in range(1, 100):
#         if i % 3 == 0:
#             three.append(i)
#             print("Делятся на 3",i)
#         if i % 5 == 0:
#             five.append(i)
#             print("Делятся на 5",i)
#         if i % 3 == 0 and i %5 ==0:
#             three_five.append(i)
#             print("Делятся обоим",i)        
#     print(three)        
#     print(five)        
#     print(three_five)        
# num()    
 
 
 
# №2            
# def num(x, y):
#     try:
#         a = x / y
#         print(a)
#     except ZeroDivisionError: 
#         print(0)  
# num(10, 2)    

# №3
def num(a):
    for i in range(a):
        print(i)
num(6)                