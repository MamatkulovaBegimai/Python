# Задача 1
def func(names, *args):
    print("Имя игрока - ",names)
    for i in args:
        print("Очки - ", i)
func("Бегимай", 45, 98, 34, 78) 


# Задача 2
def names(*args):
    for i in args:
        print(i * 2)
names(1,2,3, 4, 5)  

# Задача 3
def slovo(*args):
    for i in args:
        print(i)
slovo('Begimai', 'Meerimai', 'Syimyk', 'Adelya')               

# Задача 4
def cars(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
cars(Bekjan = "Mersedes", Beka = "Tayota")        
  

# Задача 5
def sd(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
sd(firstname = "Muntasir", lastname = "IT", age = 30, country = "USA", email =
"mun@gmail.com", phone = "0987654")        

# Задача 6
def cars(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
cars(China = "Китай", Kyrgyzstan = "", age = 30, country = "USA", email =
"mun@gmail.com", phone = "0987654")   

# Задача 7
def lexus(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
lexus(Масса = "3350", Двигатель = "Бензиновый", Разгон = "7,7")        
     
    
