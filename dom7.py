# Задача 1
# (try, except) нужен для того, чтобы обработать ошибку. Он обнаружит ошибку в программе и сообщает об этом не выходя из программы. Мы исполюзуем их для того чтобы программа работала даже если обнаружил ошибку и чтобы не случился сбой.

# Задача 2
# num1 = int(input("Введите первое число: "))
# operation = input("+, -, *, /: ")
# num2 = int(input("Введите второе число: "))
# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)   
# elif operation == "*":
#     print(num1 * num2) 
# elif operation == "/":
#     try:
#         print(num1 / num2)  
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!")  
# else:
#     print("Неправильная операция")
    
# Задача 3
# try:
#     num = (5 + '5')
#     print(num)
# except TypeError :
    # print("Ошибка типов данных! Иди читай notion")

# Задача 4
# a = input()
# b = input()
# c = a.split(":")      
# d = b.split(":")
# res_hours = (int(d[0]) - int(c[0]))*3600    
# res_mins = (int(d[1]) - int(c[1]))*60
# res = (int(d[2]) - int(c[2])) + res_hours + res_mins 
# print(res)

# Задача 5
# lst = []
# for i in range(1, 401):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst) 

# Задача 6
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

# Задача 7
# numbers = {'num_1' : 1,'num_2' : 2, 'num_3' : 3, 'num_100' : 100} 
# res = {}
# for k, v in numbers.items():
#     res.setdefault(k, v * 5)
# print(res)    
    

# Задача 8
# adilet = {'name' : 'Adilet', 'age' : 17, 'color' : 'White'}
# adilet['age'] *= 2
# print(adilet)


# Задача 9
# adilet = {'name' : 'Adilet', 'age' : 17, 'color' : 'White'}
# del adilet['color']
# print(adilet)

# Задача 10
# adilet = {'name' : 'Adilet', 'age' : 17, 'color' : 'White'}
# adilet['age'] = 18
# print(adilet)

# Задача 11
# adilet = {'name' : 'Adilet', 'age' : 17, 'color' : 'White'}
# adilet['adress'] = 'Западный Анар'
# print(adilet)
  